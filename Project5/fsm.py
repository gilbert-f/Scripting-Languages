#! /usr/bin/python

from collections import defaultdict

class State:
    def __init__(self, state_name, action_string, edge_list = []):
        self.state_name = state_name
        self.action_string = action_string
        self.edge_list = edge_list

class Edge:
    def __init__(self, event_name, next_state, optional_action_string = ""):
        self.event_name = event_name
        self.next_state = next_state
        self.optional_action_string = optional_action_string

class Machine:
    def __init__(self, machine_name):
        self.machine_name = machine_name
        self.states = defaultdict()
        self.events = defaultdict()

    def header(self, text):
        self.text_header = text

    def footer(self, text):
        self.text_footer = text

    def state(self, state_name, action_string, edge_list = []):
        state = State(state_name, action_string, edge_list)

        if not state_name in self.states.keys():
            self.states[state_name] = state
        else:
            raise Exception()

    def edge(self, event_name, next_state, optional_action_string = ""):
        edge = Edge(event_name, next_state, optional_action_string)

        self.events[event_name] = edge
        return edge

    def edges(self, *args_list):
        edges = []

        for arguments in args_list:
            edge = Edge("", "")

            i = 0
            for arg in arguments:
                if i == 0:
                    edge.event_name = arg
                elif i == 1:
                    edge.next_state = arg
                elif i == 2:
                    edge.optional_action_string = arg
                i += 1

            if edge.optional_action_string:
                self.edge(edge.event_name, edge.next_state, edge.optional_action_string)
            else:
                self.edge(edge.event_name, edge.next_state)
            edges.append(edge)
        return edges

    def gen(self):
        print self.text_header

        print "#include <iostream>\nusing namespace std;\n"

        print "enum State {"
        for key in self.states.keys():
            print "\t" + key + "_STATE,"
        print "};\n"

        print "enum Event {"
        for key in self.events.keys():
            print "\t" + key + "_EVENT,"
        print "\tINVALID_EVENT\n};\n"

        print "const char * EVENT_NAMES[] = {"
        for key in self.events.keys():
            print "\t\"" + key + "\","
        print "};\n\nEvent get_next_event();\n"

        print "Event string_to_event(string event_string) {"
        for key in self.events.keys():
            print "\tif (event_string == \"" + key + "\") {return " + key + "_EVENT;}"
        print "\treturn INVALID_EVENT;\n}\n"

        print "int " + self.machine_name + "(State initial_state) {"
        print "\tState state = initial_state;\n\tEvent event;\n\twhile (true) {\n\t\tswitch (state) {\n"

        for value in self.states.values():
            print "\t\t\tcase " + value.state_name + "_STATE:"
            print "\t\t\t\tcerr << \"state " + value.state_name + "\" << endl;"
            print value.action_string
            print "\t\t\t\tevent = get_next_event();"
            print "\t\t\t\tcerr << \"event \" << EVENT_NAMES[event] << endl;"

            print "\t\t\t\tswitch (event) {"
            if not value.edge_list:
                pass
            else:
                for edge in value.edge_list:
                    print "\n\t\t\t\tcase " + edge.event_name + "_EVENT:"
                    if edge.optional_action_string:
                        print edge.optional_action_string
                    else:
                        print
                    print "\t\t\t\t\tstate = " + edge.next_state + "_STATE;\n\t\t\t\t\tbreak;\n"

            print "\n\t\t\t\tdefault:\n\t\t\t\t\tcerr << \"INVALID EVENT \" << event << ",
            print "\" in state " + value.state_name + " \" << endl;"
            print "\t\t\t\t\treturn -1;\n\t\t\t\t}\n\t\t\t\tbreak;\n"

        print"\t\t}\n\t}\n}"
        print self.text_footer
