from surface_crns.readers.statements import section_ends
import re

'''
For external use
'''

def read_constraints(filename):
    '''
    Read constraints with the format:

    name1, name2, <distance>

    where name1, etc are any alphanumeric labels for chemical states, and <distance>
    is a number. The transition cannot happen when name1 and name2 are over <distance> apart.

    Lines beginning with '#' or '%' are treated as comments.

    The file may optionally be terminated by a line of the string
    "!END_CONSTRAINTS"
    '''
    with open(filename, 'rU') as rule_file:
        return parse_constraints_stream(rule_file)

def parse_constraints_stream(rules_stream, debug = False):
    '''
    Parse a stream of strings containing constraints
    See documentation for read_constraints for a description.
    '''
    if debug:
        print("Reading constraints... ", end = "")
    constraints = []
    for line in rules_stream:
        if line.startswith(section_ends['constraints']):
            break
        if not (line.startswith("#") or
                line.startswith("%") or
                line.strip() == ""):
            constraints.append(parse_constraint(line))
    if debug:
        print("done.")
    return constraints

'''
Internal use only
'''

def parse_constraint(line):
    tokens = line.strip().split(",")
    if len(tokens) != 3:
       raise Exception('Invalid constaint rule "' + line +
                       '": must have exactly three parts')
    if not tokens[2].isnumeric():
        raise Exception("Invalid constaint rule " + line + ": distance must be a number")

    constraint = []
    
    try:
        species1 = parse_species(tokens[0])
        constraint.append(species1)
        species2 = parse_species(tokens[1])
        constraint.append(species2)
    except:
        raise Exception('Invalid constaint rule "' + line +
                        '": species names must be alphanumeric')

    constraint.append(float(tokens[2]))

    return constraint

def parse_species(species_string):
    species_string = species_string.strip()
    if not re.match('^[,_a-zA-Z0-9]+$', species_string):
        raise SyntaxError()
    return species_string