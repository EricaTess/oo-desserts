"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__(self, name, flavor, price):
      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0

      self.cache[name] = self

    def add_stock(self, amount):

      self.qty += amount

    def sell(self, amount):

      if self.qty == 0:
        print("Sorry, these cupcakes are sold out")
        return
      if self.qty < amount:
        print("Sorry, we don't have enough cupcakes")
        qty.self = 0
        return

      self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients, amount):

      updated_ingredients = []

      for ingredient in ingredients:
        new_amount = ingredient[1] * amount
        updated_ingredients.append((ingredient, new_amount))

      return updated_ingredients


    @classmethod
    def get(cls, name):
      if name not in cls.cache:
        print("Sorry, that cupcake doesn't exist")
        return
      else:
        return cls.cache[name]
    


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
