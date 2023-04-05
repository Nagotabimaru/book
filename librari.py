# 1
import abc


class Receiver(object):

    def start(self):
        print('execute start command')

    def stop(self):
        print('execute stop command')

    def suspend(self):
        print('execute suspend command')

    def play(self):
        print('execute play command')


class Command(object):
    """
         Командный абстрактный метод, подклассы должны реализовывать метод execute
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass


class Start_command(Command):
    """командa start"""

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.start()


class Stop_command(Command):
    " командa stop "

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.stop()


class Client(object):
    """
         Клиент
    """

    def __init__(self, command):
        self.command = command

    def command_do(self):
        self.command.execute()


if __name__ == '__main__':
    receiver = Receiver()
    start_command = Start_command(receiver)
    client = Client(start_command)
    client.command_do()
    stop_command = Stop_command(receiver)
    client.command = stop_command
    client.command_do()


# 3
class Book:
    def __init__(self, bid, autor, name, year):
        self.id = bid
        self.autor = autor
        self.name = name
        try:
            self.year = int(year)
        except ValueError:
            raise ValueError('...')

    def __str__(self):
        return f'{self.id}, {self.autor}, {self.name}, {self.year}'


class Library:
    def __init__(self):
        self._storage = {}

    def __str__(self):
        result = []
        for item in self._storage.values():
            result.append(f'{str(item[0])} - {str(item[1])} экз.')
        return str(result)

    def add(self, book):
        if not isinstance(book, Book):
            raise ValueError('...')
        bid = book.id
        if bid in self._storage:
            self._storage[bid][1] += 1
        else:
            self._storage[bid] = [book, 1]

    def see(self, bid):
        item = self._storage.get(bid)
        if item:
            return item[0]
        return None

    def pop(self, bid):
        item = self._storage.get(bid)
        if item:
            item[1] -= 1
            if not item[1]:
                self._storage.pop(bid)
            return item[0]
        else:
            raise ValueError('...')

    def find(self, autor='', name='', year=0):
        result = []
        for item in self._storage.values():
            book = item[0]
            if (not autor or autor == book.autor) and \
                    (not name or book.name.startswith(name)) and \
                    (not year or year == book.year):
                result.append(book.id)
        return result


book1 = Book(1, 'Плохой К.', 'Вредные советы', 2000)
book2 = Book(1, 'Плохой К.', 'Вредные советы', 2000)
book3 = Book(5, 'Разводила В.', 'Как бытсро заработать', 2008)
book4 = Book(7, 'Смелый Я.', 'Гаси разводил!', 2009)
book5 = Book(9, 'Разводила В.', 'Как бытсро потерять деньги', 2010)
lib = Library()

lib.add(book1)
lib.add(book2)
lib.add(book3)
print(lib)
print()
print(lib.find(year=2000))

print()
lib.add(book4)
lib.add(book5)
print(lib.pop(1))
print(lib.pop(1))
print()
print(lib)
print()
