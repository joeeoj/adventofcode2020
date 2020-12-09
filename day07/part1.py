def parse_file() -> dict:
    """Parse into a dict of containing_bag -> List[bags]"""
    bags = {}
    with open('input.txt') as f:
        for row in f.readlines():
            # remove trailing period with [:-1]
            bag, insides_str = row.strip()[:-1].replace(' bags', '').replace(' bag', '').split(' contain ')

            # [2:] removes bag count, we don't need it -- we just need the presence of a containing bag
            # we also don't want 'no other'
            insides = [b.strip()[2:] for b in insides_str.strip().split(', ') if b.strip() != 'no other']

            if len(insides) > 0:
                bags[bag.strip()] = insides
    return bags

def can_contain_bag(outer_bag: str) -> bool:
    contained_bags = BAGS.get(outer_bag)

    if contained_bags is None:
        return False
    if SEARCH_BAG in contained_bags:
        return True
    for bag in contained_bags:
        if can_contain_bag(bag):
            return True


if __name__ == '__main__':
    BAGS = parse_file()
    SEARCH_BAG = 'shiny gold'

    found = [b for b in BAGS if can_contain_bag(b)]
    print(f'Answer: {len(found):,} out of {len(BAGS):,} bags')
