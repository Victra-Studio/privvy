"""
Interpreter for the Privvy programming language.
Executes the Abstract Syntax Tree.
"""

from typing import Any, Dict, List, Optional
from ast_nodes import *
import sqlite3
import sys


class ReturnValue(Exception):
    """Exception used to handle return statements."""
    def __init__(self, value):
        self.value = value


class DatabaseConnection:
    """Represents a database connection - supports PostgreSQL and SQLite."""
    
    def __init__(self, connection_string: str):
        """Initialize database connection from connection string."""
        self.connection_string = connection_string
        self.connection = None
        self.db_type = None
        
        # Determine database type and connect
        if connection_string.startswith('sqlite://') or connection_string.endswith('.db') or connection_string == ':memory:':
            self._connect_sqlite(connection_string)
        elif connection_string.startswith('postgresql://') or connection_string.startswith('postgres://'):
            self._connect_postgres(connection_string)
        else:
            raise ValueError(f"Unsupported database type. Use 'sqlite://path.db' or 'postgresql://...'")
    
    def _connect_sqlite(self, connection_string: str):
        """Connect to SQLite database."""
        self.db_type = 'sqlite'
        if connection_string.startswith('sqlite://'):
            db_path = connection_string.replace('sqlite://', '')
        else:
            db_path = connection_string
        
        try:
            self.connection = sqlite3.connect(db_path)
            self.connection.row_factory = sqlite3.Row  # Enable column name access
        except Exception as e:
            raise RuntimeError(f"Failed to connect to SQLite: {e}")
    
    def _connect_postgres(self, connection_string: str):
        """Connect to PostgreSQL database."""
        self.db_type = 'postgres'
        try:
            import psycopg2
            import psycopg2.extras
            self.connection = psycopg2.connect(connection_string)
        except ImportError:
            raise RuntimeError("PostgreSQL support requires psycopg2. Install it with: pip install psycopg2-binary")
        except Exception as e:
            raise RuntimeError(f"Failed to connect to PostgreSQL: {e}")
    
    def get(self, name: str):
        """Get a method of the database connection."""
        methods = {
            'query': self._query_method,
            'execute': self._execute_method,
            'close': self._close_method,
            'commit': self._commit_method,
            'rollback': self._rollback_method
        }
        
        if name in methods:
            return methods[name]()
        
        raise AttributeError(f"Database has no attribute '{name}'")
    
    def _query_method(self):
        """Return the query method."""
        class QueryMethod:
            def __init__(self, db_conn):
                self.db_conn = db_conn
            
            def call(self, interpreter, arguments):
                if len(arguments) < 1:
                    raise TypeError("query() requires at least 1 argument (SQL query)")
                
                sql = arguments[0]
                params = arguments[1:] if len(arguments) > 1 else []
                
                try:
                    cursor = self.db_conn.connection.cursor()
                    
                    if self.db_conn.db_type == 'postgres':
                        import psycopg2.extras
                        cursor = self.db_conn.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                    
                    cursor.execute(sql, params)
                    
                    # Fetch all results and convert to list of dicts
                    if cursor.description:
                        if self.db_conn.db_type == 'sqlite':
                            rows = cursor.fetchall()
                            return [dict(row) for row in rows]
                        else:
                            return cursor.fetchall()
                    
                    return []
                except Exception as e:
                    raise RuntimeError(f"Query failed: {e}")
        
        return QueryMethod(self)
    
    def _execute_method(self):
        """Return the execute method for INSERT/UPDATE/DELETE."""
        class ExecuteMethod:
            def __init__(self, db_conn):
                self.db_conn = db_conn
            
            def call(self, interpreter, arguments):
                if len(arguments) < 1:
                    raise TypeError("execute() requires at least 1 argument (SQL statement)")
                
                sql = arguments[0]
                params = arguments[1:] if len(arguments) > 1 else []
                
                try:
                    cursor = self.db_conn.connection.cursor()
                    cursor.execute(sql, params)
                    self.db_conn.connection.commit()
                    return cursor.rowcount
                except Exception as e:
                    self.db_conn.connection.rollback()
                    raise RuntimeError(f"Execute failed: {e}")
        
        return ExecuteMethod(self)
    
    def _close_method(self):
        """Return the close method."""
        class CloseMethod:
            def __init__(self, db_conn):
                self.db_conn = db_conn
            
            def call(self, interpreter, arguments):
                if self.db_conn.connection:
                    self.db_conn.connection.close()
                return None
        
        return CloseMethod(self)
    
    def _commit_method(self):
        """Return the commit method."""
        class CommitMethod:
            def __init__(self, db_conn):
                self.db_conn = db_conn
            
            def call(self, interpreter, arguments):
                self.db_conn.connection.commit()
                return None
        
        return CommitMethod(self)
    
    def _rollback_method(self):
        """Return the rollback method."""
        class RollbackMethod:
            def __init__(self, db_conn):
                self.db_conn = db_conn
            
            def call(self, interpreter, arguments):
                self.db_conn.connection.rollback()
                return None
        
        return RollbackMethod(self)


class ModelDefinition:
    """Represents a database model/table with ORM capabilities."""
    
    def __init__(self, table_name: str, fields: dict):
        """Initialize a model with table name and field definitions."""
        self.table_name = table_name
        self.fields = fields
    
    def get(self, name: str):
        """Get a method of the model."""
        methods = {
            'migrate': self._migrate_method,
            'create': self._create_method,
            'find': self._find_method,
            'findBy': self._find_by_method,
            'all': self._all_method,
            'where': self._where_method,
            'update': self._update_method,
            'delete': self._delete_method,
            'count': self._count_method,
            'drop': self._drop_method
        }
        
        if name in methods:
            return methods[name]()
        
        raise AttributeError(f"Model has no attribute '{name}'")
    
    def _migrate_method(self):
        """Create the table in the database."""
        class MigrateMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("migrate() requires 1 argument (database connection)")
                
                db = arguments[0]
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("migrate() requires a Database connection")
                
                # Build CREATE TABLE statement
                field_defs = []
                for field_name, field_type in self.model.fields.items():
                    field_defs.append(f"{field_name} {field_type}")
                
                fields_sql = ", ".join(field_defs)
                sql = f"CREATE TABLE IF NOT EXISTS {self.model.table_name} ({fields_sql})"
                
                db.connection.cursor().execute(sql)
                db.connection.commit()
                
                return None
        
        return MigrateMethod(self)
    
    def _create_method(self):
        """Insert a new record."""
        class CreateMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) != 2:
                    raise TypeError("create() requires 2 arguments (database, data)")
                
                db = arguments[0]
                data = arguments[1]
                
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("First argument must be a Database connection")
                if not isinstance(data, dict):
                    raise TypeError("Second argument must be a dictionary")
                
                # Build INSERT statement
                columns = list(data.keys())
                placeholders = ["?" if db.db_type == "sqlite" else "%s"] * len(columns)
                values = [data[col] for col in columns]
                
                sql = f"INSERT INTO {self.model.table_name} ({', '.join(columns)}) VALUES ({', '.join(placeholders)})"
                
                cursor = db.connection.cursor()
                cursor.execute(sql, values)
                db.connection.commit()
                
                # Return the inserted ID
                if db.db_type == "sqlite":
                    return cursor.lastrowid
                else:
                    return cursor.lastrowid if hasattr(cursor, 'lastrowid') else None
        
        return CreateMethod(self)
    
    def _find_method(self):
        """Find a record by ID."""
        class FindMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) != 2:
                    raise TypeError("find() requires 2 arguments (database, id)")
                
                db = arguments[0]
                record_id = arguments[1]
                
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("First argument must be a Database connection")
                
                # Query for the record
                placeholder = "?" if db.db_type == "sqlite" else "%s"
                sql = f"SELECT * FROM {self.model.table_name} WHERE id = {placeholder}"
                
                cursor = db.connection.cursor()
                
                if db.db_type == 'postgres':
                    import psycopg2.extras
                    cursor = db.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
                cursor.execute(sql, (record_id,))
                
                if db.db_type == 'sqlite':
                    row = cursor.fetchone()
                    return dict(row) if row else None
                else:
                    return cursor.fetchone()
        
        return FindMethod(self)
    
    def _find_by_method(self):
        """Find records by field value."""
        class FindByMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) != 3:
                    raise TypeError("findBy() requires 3 arguments (database, field, value)")
                
                db = arguments[0]
                field = arguments[1]
                value = arguments[2]
                
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("First argument must be a Database connection")
                
                placeholder = "?" if db.db_type == "sqlite" else "%s"
                sql = f"SELECT * FROM {self.model.table_name} WHERE {field} = {placeholder}"
                
                cursor = db.connection.cursor()
                
                if db.db_type == 'postgres':
                    import psycopg2.extras
                    cursor = db.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
                cursor.execute(sql, (value,))
                
                if db.db_type == 'sqlite':
                    rows = cursor.fetchall()
                    return [dict(row) for row in rows]
                else:
                    return cursor.fetchall()
        
        return FindByMethod(self)
    
    def _all_method(self):
        """Get all records."""
        class AllMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("all() requires 1 argument (database)")
                
                db = arguments[0]
                
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("Argument must be a Database connection")
                
                sql = f"SELECT * FROM {self.model.table_name}"
                
                cursor = db.connection.cursor()
                
                if db.db_type == 'postgres':
                    import psycopg2.extras
                    cursor = db.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
                cursor.execute(sql)
                
                if db.db_type == 'sqlite':
                    rows = cursor.fetchall()
                    return [dict(row) for row in rows]
                else:
                    return cursor.fetchall()
        
        return AllMethod(self)
    
    def _where_method(self):
        """Query with WHERE conditions."""
        class WhereMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) < 2:
                    raise TypeError("where() requires at least 2 arguments (database, sql_condition, ...params)")
                
                db = arguments[0]
                condition = arguments[1]
                params = arguments[2:] if len(arguments) > 2 else []
                
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("First argument must be a Database connection")
                
                sql = f"SELECT * FROM {self.model.table_name} WHERE {condition}"
                
                cursor = db.connection.cursor()
                
                if db.db_type == 'postgres':
                    import psycopg2.extras
                    cursor = db.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
                cursor.execute(sql, params)
                
                if db.db_type == 'sqlite':
                    rows = cursor.fetchall()
                    return [dict(row) for row in rows]
                else:
                    return cursor.fetchall()
        
        return WhereMethod(self)
    
    def _update_method(self):
        """Update a record by ID."""
        class UpdateMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) != 3:
                    raise TypeError("update() requires 3 arguments (database, id, data)")
                
                db = arguments[0]
                record_id = arguments[1]
                data = arguments[2]
                
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("First argument must be a Database connection")
                if not isinstance(data, dict):
                    raise TypeError("Third argument must be a dictionary")
                
                # Build UPDATE statement
                placeholder = "?" if db.db_type == "sqlite" else "%s"
                set_clauses = [f"{col} = {placeholder}" for col in data.keys()]
                values = list(data.values()) + [record_id]
                
                sql = f"UPDATE {self.model.table_name} SET {', '.join(set_clauses)} WHERE id = {placeholder}"
                
                cursor = db.connection.cursor()
                cursor.execute(sql, values)
                db.connection.commit()
                
                return cursor.rowcount
        
        return UpdateMethod(self)
    
    def _delete_method(self):
        """Delete a record by ID."""
        class DeleteMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) != 2:
                    raise TypeError("delete() requires 2 arguments (database, id)")
                
                db = arguments[0]
                record_id = arguments[1]
                
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("First argument must be a Database connection")
                
                placeholder = "?" if db.db_type == "sqlite" else "%s"
                sql = f"DELETE FROM {self.model.table_name} WHERE id = {placeholder}"
                
                cursor = db.connection.cursor()
                cursor.execute(sql, (record_id,))
                db.connection.commit()
                
                return cursor.rowcount
        
        return DeleteMethod(self)
    
    def _count_method(self):
        """Count records."""
        class CountMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("count() requires 1 argument (database)")
                
                db = arguments[0]
                
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("Argument must be a Database connection")
                
                sql = f"SELECT COUNT(*) as count FROM {self.model.table_name}"
                
                cursor = db.connection.cursor()
                
                if db.db_type == 'sqlite':
                    cursor.row_factory = sqlite3.Row
                
                cursor.execute(sql)
                result = cursor.fetchone()
                
                if db.db_type == 'sqlite':
                    return dict(result)['count']
                else:
                    return result[0]
        
        return CountMethod(self)
    
    def _drop_method(self):
        """Drop the table."""
        class DropMethod:
            def __init__(self, model):
                self.model = model
            
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("drop() requires 1 argument (database)")
                
                db = arguments[0]
                
                if not isinstance(db, DatabaseConnection):
                    raise TypeError("Argument must be a Database connection")
                
                sql = f"DROP TABLE IF EXISTS {self.model.table_name}"
                
                cursor = db.connection.cursor()
                cursor.execute(sql)
                db.connection.commit()
                
                return None
        
        return DropMethod(self)


class Environment:
    """Represents a lexical environment for variable storage."""
    
    def __init__(self, parent: Optional['Environment'] = None):
        self.parent = parent
        self.variables: Dict[str, Any] = {}
    
    def define(self, name: str, value: Any):
        """Define a new variable in this environment."""
        self.variables[name] = value
    
    def get(self, name: str) -> Any:
        """Get a variable value."""
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise NameError(f"Undefined variable: {name}")
    
    def set(self, name: str, value: Any):
        """Set a variable value."""
        if name in self.variables:
            self.variables[name] = value
        elif self.parent:
            self.parent.set(name, value)
        else:
            raise NameError(f"Undefined variable: {name}")


class PrivvyFunction:
    """Represents a Privvy function."""
    
    def __init__(self, declaration: FunctionDeclaration, closure: Environment):
        self.declaration = declaration
        self.closure = closure
    
    def call(self, interpreter: 'Interpreter', arguments: List[Any]) -> Any:
        """Execute the function."""
        # Create new environment for function execution
        env = Environment(self.closure)
        
        # Bind parameters
        if len(arguments) != len(self.declaration.parameters):
            raise TypeError(f"Function {self.declaration.name} expects {len(self.declaration.parameters)} arguments, got {len(arguments)}")
        
        for i, param in enumerate(self.declaration.parameters):
            env.define(param, arguments[i])
        
        # Execute function body
        try:
            interpreter.execute_block(self.declaration.body, env)
        except ReturnValue as ret:
            return ret.value
        
        return None


class PrivvyClass:
    """Represents a Privvy class."""
    
    def __init__(self, name: str, superclass: Optional['PrivvyClass'], 
                 constructor: Optional[PrivvyFunction], methods: Dict[str, PrivvyFunction]):
        self.name = name
        self.superclass = superclass
        self.constructor = constructor
        self.methods = methods
    
    def call(self, interpreter: 'Interpreter', arguments: List[Any]) -> 'PrivvyInstance':
        """Instantiate the class."""
        instance = PrivvyInstance(self)
        
        # Call constructor if it exists
        if self.constructor:
            # Bind 'this' to the instance
            bound_env = Environment(self.constructor.closure)
            bound_env.define('this', instance)
            
            if len(arguments) != len(self.constructor.declaration.parameters):
                raise TypeError(f"Constructor expects {len(self.constructor.declaration.parameters)} arguments, got {len(arguments)}")
            
            for i, param in enumerate(self.constructor.declaration.parameters):
                bound_env.define(param, arguments[i])
            
            try:
                interpreter.execute_block(self.constructor.declaration.body, bound_env)
            except ReturnValue:
                pass  # Constructors don't return values
        
        return instance
    
    def find_method(self, name: str) -> Optional[PrivvyFunction]:
        """Find a method in this class or superclass."""
        if name in self.methods:
            return self.methods[name]
        elif self.superclass:
            return self.superclass.find_method(name)
        return None


class PrivvyInstance:
    """Represents an instance of a Privvy class."""
    
    def __init__(self, klass: PrivvyClass):
        self.klass = klass
        self.fields: Dict[str, Any] = {}
    
    def get(self, name: str) -> Any:
        """Get a property or method."""
        if name in self.fields:
            return self.fields[name]
        
        method = self.klass.find_method(name)
        if method:
            return self.bind_method(method)
        
        raise AttributeError(f"Undefined property: {name}")
    
    def set(self, name: str, value: Any):
        """Set a property."""
        self.fields[name] = value
    
    def bind_method(self, method: PrivvyFunction) -> PrivvyFunction:
        """Bind a method to this instance."""
        # Create a new environment with 'this' bound to this instance
        env = Environment(method.closure)
        env.define('this', self)
        return PrivvyFunction(method.declaration, env)


class Interpreter:
    """Interprets and executes Privvy AST."""
    
    def __init__(self):
        self.globals = Environment()
        self.environment = self.globals
        
        # Define built-in functions
        self.define_builtins()
    
    def define_builtins(self):
        """Define built-in functions."""
        # print function
        class PrintFunction:
            def call(self, interpreter, arguments):
                output = ' '.join(str(arg) for arg in arguments)
                print(output)
                return None
        
        self.globals.define('print', PrintFunction())
        
        # len function
        class LenFunction:
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("len() takes exactly 1 argument")
                arg = arguments[0]
                if isinstance(arg, (list, str)):
                    return len(arg)
                raise TypeError(f"len() not supported for {type(arg).__name__}")
        
        self.globals.define('len', LenFunction())
        
        # str function
        class StrFunction:
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("str() takes exactly 1 argument")
                return str(arguments[0])
        
        self.globals.define('str', StrFunction())
        
        # int function
        class IntFunction:
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("int() takes exactly 1 argument")
                try:
                    return int(arguments[0])
                except ValueError:
                    raise ValueError(f"Cannot convert {arguments[0]} to int")
        
        self.globals.define('int', IntFunction())
        
        # float function
        class FloatFunction:
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("float() takes exactly 1 argument")
                try:
                    return float(arguments[0])
                except ValueError:
                    raise ValueError(f"Cannot convert {arguments[0]} to float")
        
        self.globals.define('float', FloatFunction())
        
        # dict function - create dictionary from array of key-value pairs
        class DictFunction:
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("dict() takes exactly 1 argument (array of key-value pairs)")
                
                arr = arguments[0]
                if not isinstance(arr, list):
                    raise TypeError("dict() argument must be an array")
                
                if len(arr) % 2 != 0:
                    raise ValueError("dict() array must have even length (key-value pairs)")
                
                result = {}
                for i in range(0, len(arr), 2):
                    key = arr[i]
                    value = arr[i + 1]
                    result[key] = value
                
                return result
        
        self.globals.define('dict', DictFunction())
        
        # Database class
        class DatabaseClass:
            """Built-in Database class for easy database access."""
            def call(self, interpreter, arguments):
                if len(arguments) != 1:
                    raise TypeError("Database() takes exactly 1 argument (connection string)")
                return DatabaseConnection(arguments[0])
        
        self.globals.define('Database', DatabaseClass())
        
        # Model function for ORM
        class ModelFunction:
            """Built-in Model function for ORM."""
            def call(self, interpreter, arguments):
                if len(arguments) != 2:
                    raise TypeError("Model() takes exactly 2 arguments (table_name, fields)")
                
                table_name = arguments[0]
                fields = arguments[1]
                
                if not isinstance(table_name, str):
                    raise TypeError("First argument must be a string (table name)")
                if not isinstance(fields, dict):
                    raise TypeError("Second argument must be a dictionary (field definitions)")
                
                return ModelDefinition(table_name, fields)
        
        self.globals.define('Model', ModelFunction())
    
    def interpret(self, program: Program):
        """Interpret a program."""
        try:
            for statement in program.statements:
                self.execute(statement)
        except ReturnValue as ret:
            raise RuntimeError("Cannot use 'return' outside a function")
    
    def execute(self, node: ASTNode) -> Any:
        """Execute a statement or evaluate an expression."""
        
        # Literals
        if isinstance(node, NumberLiteral):
            return node.value
        
        elif isinstance(node, StringLiteral):
            return node.value
        
        elif isinstance(node, BooleanLiteral):
            return node.value
        
        elif isinstance(node, NullLiteral):
            return None
        
        # Identifier
        elif isinstance(node, Identifier):
            return self.environment.get(node.name)
        
        # Binary operations
        elif isinstance(node, BinaryOp):
            left = self.execute(node.left)
            right = self.execute(node.right)
            
            if node.operator == '+':
                return left + right
            elif node.operator == '-':
                return left - right
            elif node.operator == '*':
                return left * right
            elif node.operator == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                return left / right
            elif node.operator == '%':
                return left % right
            elif node.operator == '==':
                return left == right
            elif node.operator == '!=':
                return left != right
            elif node.operator == '<':
                return left < right
            elif node.operator == '<=':
                return left <= right
            elif node.operator == '>':
                return left > right
            elif node.operator == '>=':
                return left >= right
            elif node.operator == 'and':
                return self.is_truthy(left) and self.is_truthy(right)
            elif node.operator == 'or':
                return left if self.is_truthy(left) else right
        
        # Unary operations
        elif isinstance(node, UnaryOp):
            operand = self.execute(node.operand)
            
            if node.operator == '-':
                return -operand
            elif node.operator == 'not' or node.operator == '!':
                return not self.is_truthy(operand)
        
        # Variable declaration
        elif isinstance(node, VarDeclaration):
            value = None
            if node.initializer:
                value = self.execute(node.initializer)
            self.environment.define(node.name, value)
            return None
        
        # Assignment
        elif isinstance(node, Assignment):
            value = self.execute(node.value)
            
            if isinstance(node.target, Identifier):
                self.environment.set(node.target.name, value)
            elif isinstance(node.target, MemberAccess):
                obj = self.execute(node.target.object)
                if isinstance(obj, PrivvyInstance):
                    obj.set(node.target.property, value)
                else:
                    raise TypeError("Cannot set property on non-object")
            elif isinstance(node.target, ArrayAccess):
                array = self.execute(node.target.array)
                index = self.execute(node.target.index)
                if isinstance(array, list):
                    array[int(index)] = value
                else:
                    raise TypeError("Cannot index non-array")
            
            return value
        
        # Function call
        elif isinstance(node, FunctionCall):
            callee = self.execute(node.callee)
            arguments = [self.execute(arg) for arg in node.arguments]
            
            if hasattr(callee, 'call'):
                return callee.call(self, arguments)
            else:
                raise TypeError(f"'{callee}' is not callable")
        
        # Member access
        elif isinstance(node, MemberAccess):
            obj = self.execute(node.object)
            
            if isinstance(obj, PrivvyInstance):
                return obj.get(node.property)
            elif isinstance(obj, DatabaseConnection):
                return obj.get(node.property)
            elif isinstance(obj, ModelDefinition):
                return obj.get(node.property)
            else:
                raise TypeError(f"Cannot access property on {type(obj).__name__}")
        
        # Array literal
        elif isinstance(node, ArrayLiteral):
            return [self.execute(elem) for elem in node.elements]
        
        # Array access
        elif isinstance(node, ArrayAccess):
            array = self.execute(node.array)
            index = self.execute(node.index)
            
            if isinstance(array, list):
                return array[int(index)]
            elif isinstance(array, str):
                return array[int(index)]
            elif isinstance(array, dict):
                # Support dictionary access
                return array[index]
            else:
                raise TypeError("Cannot index non-array")
        
        # Function declaration
        elif isinstance(node, FunctionDeclaration):
            function = PrivvyFunction(node, self.environment)
            self.environment.define(node.name, function)
            return None
        
        # Class declaration
        elif isinstance(node, ClassDeclaration):
            superclass = None
            if node.superclass:
                superclass_value = self.environment.get(node.superclass)
                if not isinstance(superclass_value, PrivvyClass):
                    raise TypeError(f"Superclass must be a class")
                superclass = superclass_value
            
            constructor = None
            if node.constructor:
                constructor = PrivvyFunction(node.constructor, self.environment)
            
            methods = {}
            for method in node.methods:
                methods[method.name] = PrivvyFunction(method, self.environment)
            
            klass = PrivvyClass(node.name, superclass, constructor, methods)
            self.environment.define(node.name, klass)
            return None
        
        # If statement
        elif isinstance(node, IfStatement):
            condition = self.execute(node.condition)
            
            if self.is_truthy(condition):
                self.execute_block(node.then_branch, Environment(self.environment))
            elif node.else_branch:
                self.execute_block(node.else_branch, Environment(self.environment))
            
            return None
        
        # While loop
        elif isinstance(node, WhileStatement):
            while self.is_truthy(self.execute(node.condition)):
                self.execute_block(node.body, Environment(self.environment))
            return None
        
        # For loop
        elif isinstance(node, ForStatement):
            loop_env = Environment(self.environment)
            
            # Initializer
            if node.initializer:
                prev_env = self.environment
                self.environment = loop_env
                self.execute(node.initializer)
                self.environment = prev_env
            
            # Loop
            while True:
                # Check condition
                if node.condition:
                    prev_env = self.environment
                    self.environment = loop_env
                    condition_result = self.execute(node.condition)
                    self.environment = prev_env
                    
                    if not self.is_truthy(condition_result):
                        break
                
                # Execute body
                self.execute_block(node.body, Environment(loop_env))
                
                # Increment
                if node.increment:
                    prev_env = self.environment
                    self.environment = loop_env
                    self.execute(node.increment)
                    self.environment = prev_env
            
            return None
        
        # Return statement
        elif isinstance(node, ReturnStatement):
            value = None
            if node.value:
                value = self.execute(node.value)
            raise ReturnValue(value)
        
        # This expression
        elif isinstance(node, ThisExpression):
            return self.environment.get('this')
        
        # New expression
        elif isinstance(node, NewExpression):
            klass = self.environment.get(node.class_name)
            
            if not isinstance(klass, PrivvyClass):
                raise TypeError(f"'{node.class_name}' is not a class")
            
            arguments = [self.execute(arg) for arg in node.arguments]
            return klass.call(self, arguments)
        
        else:
            raise RuntimeError(f"Unknown AST node type: {type(node).__name__}")
    
    def execute_block(self, statements: List[ASTNode], environment: Environment):
        """Execute a block of statements in a given environment."""
        previous = self.environment
        try:
            self.environment = environment
            for statement in statements:
                self.execute(statement)
        finally:
            self.environment = previous
    
    def is_truthy(self, value: Any) -> bool:
        """Determine if a value is truthy."""
        if value is None or value is False:
            return False
        if value == 0 or value == "":
            return False
        return True

