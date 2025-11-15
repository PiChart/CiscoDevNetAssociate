import yaml
with open('YAML/r1.yaml') as file:
#yaml files can end in .yaml or .yml
    data = yaml.safe_load(file)
    # load operation can expose security risks if from untrusted sources
    # safe_load mitigates some of those risks by limiting to simple Python objects

print(data)

#applications like ansible usually handle yaml to dict conversions for you
#often will not need to use import yaml and do it yourself
#json.dump(s) and xmltodict are more relevant in the real world