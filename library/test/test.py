def hasLocalFactVersion(facts, localfact, version):
    if not isinstance(facts, dict):
        return False
    if facts.has_key(localfact) and facts[localfact].has_key('version') and facts[localfact]['version'] == version :
        return True
    return False

class TestModule(object):
    def tests(self):
        return {
            'hasLocalFactVersion': hasLocalFactVersion
        }