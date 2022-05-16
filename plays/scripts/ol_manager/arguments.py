#!/usr/bin/python
import argparse


parser = argparse.ArgumentParser(description='Satellite helper')

parser.add_argument(
    'username',
    type=str,
    help='Satellite username'
    )

parser.add_argument(
    'password',
    type=str,
    help='Satellite password'
    )

parser.add_argument(
    'api_url',
    type=str,
    help='Satellite API URL'
    )

parser.add_argument(
    '-s', '--search-hostname',
    dest='hostname',
    type=str,
    help='Enter hostname you want to search for'
    )
parser.add_argument(
    '-v', '--verify',
        dest='verify', 
        help='Enter a hostname to check if system is aleready registered: Returns bool'
        )
parser.add_argument(
    '-l', '--list-all-systems', 
    dest='all_systems', 
    action='store_true', 
    help='list all systems'
    )
parser.add_argument(
    '-g', '--get-call-list', 
    dest='get_call_list', 
    action='store_true', 
    help='get call list'
    )

parser.add_argument(
    '--get-namespace-methods', 
    dest='namespace_methods',
    help='list methods for a certain name space e.g "system"'
    )

args = parser.parse_args()





