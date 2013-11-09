class SwitchManager(object):
    def extract_all_nodes(self, content):
        return [e['node'] for e in content['nodeProperties']]

    def extract_all_properties(self, content):
        pass
