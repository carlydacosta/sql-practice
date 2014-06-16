#!/bin/env python

import sql_problem
import readline
import sys
import pickle
import sqlite3

def show_problem(problem, problem_num):
    print "Problem %d"%problem_num
    print problem['instruction']

def intro():
    print """\
Introductory SQL exercise. You will write a series of SQL queries accomplishing
different tasks. Each problem will include a link to a SQLZoo tutorial that
illustrates the concepts required, as well as a link to syntax reference for
the kind of query you'll be doing.

Type 'help' without quotes for a list of the available commands.

It will be helpful to refer to the list of tables, found by typing in 'tables',
or viewing the schema of a given table, (ex: schema orders) while formulating
your queries. If you get very stuck each problem includes a hint on how to
formulate your query, accessed by typing 'hint'.
"""
    print ""
    

def repl(cursor, problem, problem_num):
    raw_input("[ Press Enter to continue ]")
    show_problem(problem, problem_num)
    while True:
        line = raw_input("SQL> ")
        line.strip()
        
        if not line:
            continue

        tokens = line.split()

        if tokens[0] in ["q", "exit", "quit"]:
            sys.exit(0)

        elif tokens[0] == "problem":
            show_problem(problem, problem_num)

        elif tokens[0] == "hint":
            print problem['hint']
        elif tokens[0] == "tables":
            tables(cursor)
        elif tokens[0] == "schema":
            schema(tokens, cursor)
        elif tokens[0] == "help":
            help()
        elif tokens[0] == "next":
            print "Skipping problem %d"%problem_num
            return
        else:
            result = execute(line, problem, cursor)
            if result:
                show_success(line)
                return

def show_success(line):
    print "\n\tCorrect!"
    print "\t",line
    print "\tMoving on...\n"

def execute(line, problem, cursor):
    try:
        cursor.execute(line)
        results = cursor.fetchmany() 
    except sqlite3.OperationalError, e:
        print "There was a problem with your sql syntax:\n\n\t%s\n"%e
        return

    result_str = sql_problem.result_to_str(results)
    print result_str
    return sql_problem.check_solution(problem, result_str)

def tables(cursor):
    query = """select name from sqlite_master where type='table';"""
    try: 
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.OperationalError, e:
        print "There was a problem getting the table list:\n\n\t%s\n"%e
        return

    results.remove((u"alembic_version",))

    output = sql_problem.result_to_str(results)
    print "The following tables are available:\n", output

def help():
    print """The following commands are available:

    problem - Show the current problem statement
    hint - Show a hint about how to formulate the query
    tables - Show all the tables available in the database
    schema <table_name> - Show the schema used to define a given table
    next - Skip the current problem
    quit - Quit the program

Any other commands will be interpreted as a sql query and executed against the
problem set database."""


def schema(tokens, cursor):
    if len(tokens) < 2:
        print "Please indicate a table name"
        return

    table_name = tokens[1]
    query = """select sql from sqlite_master where type='table' and name=?""";
    try: 
        cursor.execute(query, (table_name,))
        results = cursor.fetchall()
    except sqlite3.OperationalError, e:
        print "There was a problem getting the table schema:\n\n\t%s\n"%e
        return

    output = sql_problem.result_to_str(results)
    if not output:
        print "No such table: %s"%table_name
        return

    print output

def load_problems():
    with open("problem_set.pickle") as f:
        return pickle.load(f)

def main():
    cursor = sql_problem.connect()
    problems = load_problems()
    intro()
    for idx, problem in enumerate(problems):
        repl(cursor, problem, idx+1)

if __name__ == "__main__":
    main()
