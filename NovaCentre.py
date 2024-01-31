import xml.etree.ElementTree as ET

class NovaCentre:
    def __init__(self):
        self.game_state = {
            'location': 'start',
            'inventory': []
        }
        self.game_world = {}

    def load_world(self, xml_file):
        tree = ET.parse(xml_file)
        self.game_world = self.parse_xml(tree.getroot())

    def parse_xml(self, root_element):
        world = {}
        for location in root_element.findall('location'):
            loc_id = location.get('id')
            loc_description = location.get('description')
            loc_data = {
                'description': loc_description,
                'connections': {},
                'items': {}
            }
            
            for connection in location.findall('connection'):
                loc_data['connections'][connection.get('to')] = connection.get('location')
            
            for item in location.findall('item'):
                item_name = item.get('name')
                item_description = item.get('description')
                loc_data['items'][item_name] = item_description
            
            world[loc_id] = loc_data

        return world

    def process_input(self, user_input):
        commands = user_input.lower().split()
        if not commands:
            return "You need to enter a command."
        
        if commands[0] == 'look':
            return self.handle_look()
        elif commands[0] == 'go':
            return self.handle_go(commands[1:])
        elif commands[0] == 'take':
            return self.handle_take(commands[1:])
        else:
            return "I don't understand that command."

    def handle_look(self):
        location = self.game_state['location']
        location_data = self.game_world.get(location, {})
        return location_data.get('description', 'There is nothing special here.')

    def handle_go(self, direction):
        if not direction:
            return "Go where?"
        direction = direction[0]
        current_location = self.game_state['location']
        new_location = self.game_world[current_location]['connections'].get(direction)
        if new_location:
            self.game_state['location'] = new_location
            return f"You go {direction} to {new_location}."
        else:
            return "You can't go that way."

    def handle_take(self, item):
        if not item:
            return "Take what?"
        item = item[0]
        current_location = self.game_state['location']
        if item in self.game_world[current_location]['items']:
            self.game_state['inventory'].append(item)
            del self.game_world[current_location]['items'][item]
            return f"You take the {item}."
        else:
            return f"There is no {item} here to take."

    def run(self):
        print("Welcome to the Text Adventure!")
        while True:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                print("Exiting game.")
                break
            output = self.process_input(user_input)
            print(output)

# Example usage
game = NovaCentre()
game.load_world('game_world.xml')
game.run()