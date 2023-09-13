from page_analyzer.app import app, ROOT
from page_analyzer.psql_db import execute_sql_script


__all__ = [
    'app',
    'execute_sql_script',
    'ROOT'
]
