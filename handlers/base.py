from handlers import settings

def org_scoped_rule(rule):
    if settings.MULTI_ORG:
        return "/<org_slug>{}".format(rule)

    return rule