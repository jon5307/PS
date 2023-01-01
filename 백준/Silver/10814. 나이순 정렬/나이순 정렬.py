from sys import stdin
from collections import namedtuple
input = stdin.readline

Person = namedtuple("Person", "age name")

users = int(input())
people = []
for _ in range(users):
    age, name = input().split()
    people.append(Person(int(age),name))

people.sort(key=lambda x : x.age)

for i in range(users):
    print(people[i].age, people[i].name)
