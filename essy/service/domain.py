_DEV_DOMAINS = {"example.com"}


def create(domain: str):
    _DEV_DOMAINS.add(domain)


def delete(domain: str):
    _DEV_DOMAINS.remove(domain)


def exists(domain: str) -> bool:
    return domain in _DEV_DOMAINS


def all_domains() -> list[str]:
    return sorted(_DEV_DOMAINS)


# TODO replace with proper methods like below
# def create(domain: str):
#     raise NotImplementedError  # todo
#
#
# def delete(domain: str):
#     raise NotImplementedError  # todo
#
#
# def exists(domain: str) -> bool:
#     raise NotImplementedError  # todo
#
#
# def all_domains() -> list[str]:
#     raise NotImplementedError  # todo
