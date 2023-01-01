from sys import stdin
from dataclasses import dataclass
input = stdin.readline

@dataclass(order=True)
class Person:
    age: int
    order: int
    name: str

users = int(input())
people = []
for i in range(users):
    age, name = input().split()
    people.append(Person(int(age),i,name))

people.sort()

for i in range(users):
    print(people[i].age, people[i].name)
