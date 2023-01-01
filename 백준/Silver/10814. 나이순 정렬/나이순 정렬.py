from sys import stdin
from typing import NamedTuple
input = stdin.readline

class Person( NamedTuple):
    age: int
    name: str

users = int(input())
people = []
for _ in range(users):
    age, name = input().split()
    people.append(Person(int(age),name))

people.sort(key=lambda x : x.age)

for i in range(users):
    print(people[i].age, people[i].name)
