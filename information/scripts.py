from information.models import Company, Food, Tag, Person


def import_company_json(company_json_obj):
    issue_list = []
    num_companies_created = 0

    if not isinstance(company_json_obj, list):
        raise TypeError("Requires a list input")

    for company in company_json_obj:
        index = company.get('index')
        name = company.get('company')
        if not index and not (index == 0):
            issue_list.append(f"Company: {company} missing 'index' key.")
        elif not name:
            issue_list.append(f"Company: {company} missing 'company' key.")
        else:
            if Company.objects.filter(index=index, name=name).exists():
                issue_list.append(f"Company: {company} already exists.")
            else:
                Company.objects.create(index=index, name=name)
                num_companies_created+=1

    return issue_list, num_companies_created


def import_people_json(people_json_obj):
    issue_list = []
    num_people_created = 0

    if not isinstance(people_json_obj, list):
        raise TypeError("Requires a list input")

    # TODO: import People file

    return issue_list, num_people_created
