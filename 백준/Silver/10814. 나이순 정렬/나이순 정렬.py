from sys import stdin
from dataclasses import dataclass
input = stdin.readline

@dataclass
class Person:
    age: int
    order: int
    name: str

users = int(input())
people = []
for i in range(users):
    age, name = input().split()
    people.append(Person(int(age),i,name))

people.sort(key=lambda x : x.age)

for i in range(users):
    print(people[i].age, people[i].name)
