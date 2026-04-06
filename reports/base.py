class BaseReport:
    """
    base abstract class
    """

    def generate(self, data: list[dict]):
        raise NotImplementedError
