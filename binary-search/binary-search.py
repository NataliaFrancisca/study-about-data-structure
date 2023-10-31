names = [
    "Aiden", "Aria", "Benjamin", "Brooklyn", "Caleb", "Charlotte", "Chloe", "Christopher", "Claire", "Daniel",
    "Ella", "Emily", "Emma", "Ethan", "Evelyn", "Grace", "Hailey", "Harper", "Isabella", "Jackson", "James",
    "Katherine", "Kaylee", "Landon", "Liam", "Lily", "Logan", "Lucas", "Mason", "Matthew", "Mia", "Michael",
    "Nathan", "Nicholas", "Noah", "Oliver", "Olivia", "Owen", "Samuel", "Sarah", "Sophia", "Thomas", "Victoria",
    "William"
];

# numbers = [2,3,4,5,6,7,8,9,12,16,18,23,28,40,50];

name_search = "William";
init = 0;
final = len(names) - 1;
operations = 0;

while(init <= final):
  meio = int((final + init) / 2);
  atual = names[meio];
  
  if(atual == name_search):
    print("NOME ENCONTRADO NA LISTA:", atual);
    break;
  
  if(atual > name_search):
    final = meio - 1;
  
  if(atual < name_search):
    init = meio + 1;
  
  operations+=1;
  

print("NÚMERO DE OPERAÇÕES:", operations);