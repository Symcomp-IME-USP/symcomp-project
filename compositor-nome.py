
import csv

divas = [
    {
      "nome": "Ana Cristina",
      "sobrenome": "Viera de Melo",
      "descrição": ""
    },
    {
      "nome": "Cristina",  
      "sobrenome": "Fernandes",
      "descrição": ""
    },
    {
      "nome": "Kelly",
      "sobrenome": "Braghetto",
      "descrição": ""
    },
    {
      "nome": "Leliane",  
      "sobrenome": "Nunes de Barros",
      "descrição": ""
    },
    {
      "nome": "Nami",
      "sobrenome": "Kobayashi",
      "descrição": ""
    },
    {
      "nome": "Nina Sumiko",  
      "sobrenome": "Tomita Hirata",
      "descrição": ""
    },
    {
      "nome": "Renata",
      "sobrenome": "Wassermann",
      "descrição": ""
    },
    {
      "nome": "Yoshiko",  
      "sobrenome": "Wakabayashi",
      "descrição": ""
    },
    {
        "nome": "Ada",
        "sobrenome": "Lovelace",
        "descrição": ""
    },
    {
        "nome": "Grace",
        "sobrenome": "Hopper",
        "descrição": ""
    },
    {
        "nome": "Radia",
        "sobrenome": "Perlman",
        "descrição": ""
    },
    {
        "nome": "Frances",
        "sobrenome": "Allen",
        "descrição": ""
    },
    {
        "nome": "Barbara",
        "sobrenome": "Liskov",
        "descrição": ""
    },
    {
        "nome": "Marissa",
        "sobrenome": "Mayer",
        "descrição": ""
    },
    {
        "nome": "Shafi",
        "sobrenome": "Ibrahim",
        "descrição": ""
    },
    {
        "nome": "Dorothy",
        "sobrenome": "Vaughan",
        "descrição": ""
    },
    {
        "nome": "Sister Mary Kenneth",
        "sobrenome": "Keller",
        "descrição": ""
    },
    {
        "nome": "Annie",
        "sobrenome": "Easley",
        "descrição": ""
    },
    {
        "nome": "Margaret",
        "sobrenome": "Hamilton",
        "descrição": ""
    },
    {
        "nome": "Lynn",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Adele",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Fei-Fei",
        "sobrenome": "Koller",
        "descrição": ""
    },
    {
        "nome": "Daphne",
        "sobrenome": "Katabi",
        "descrição": ""
    },
    {
        "nome": "Dina",
        "sobrenome": "Gebru",
        "descrição": ""
    },
    {
        "nome": "Timnit",
        "sobrenome": "Lynch",
        "descrição": ""
    },
    {
        "nome": "Nancy",
        "sobrenome": "Widom",
        "descrição": ""
    },
    {
        "nome": "Jennifer",
        "sobrenome": "Seneff",
        "descrição": ""
    },
    {
        "nome": "Stephanie",
        "sobrenome": "Sieckenius",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Asakawa",
        "descrição": ""
    },
    {
        "nome": "Chieko",
        "sobrenome": "Denton",
        "descrição": ""
    },
    {
        "nome": "Denice",
        "sobrenome": "Greif",
        "descrição": ""
    },
    {
        "nome": "Mary Jane",
        "sobrenome": "Irwin",
        "descrição": ""
    },
    {
        "nome": "Irene",
        "sobrenome": "Norris-Grey",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Bryant",
        "descrição": ""
    },
    {
        "nome": "Trudy",
        "sobrenome": "Klawe",
        "descrição": ""
    },
    {
        "nome": "Kimberly",
        "sobrenome": "Saujani",
        "descrição": ""
    },
    {
        "nome": "Maria",
        "sobrenome": "Borg",
        "descrição": ""
    },
    {
        "nome": "Reshma",
        "sobrenome": "Clark",
        "descrição": ""
    },
    {
        "nome": "Anita",
        "sobrenome": "Wilkes",
        "descrição": ""
    },
    {
        "nome": "Joan",
        "sobrenome": "Lamarr",
        "descrição": ""
    },
    {
        "nome": "Mary",
        "sobrenome": "Perlman",
        "descrição": ""
    },
    {
        "nome": "Hedy",
        "sobrenome": "Conway",
        "descrição": ""
    },
        {
        "nome": "Barbara",
        "sobrenome": "Allen",
        "descrição": ""
    },
    {
        "nome": "Radia",
        "sobrenome": "Liskov",
        "descrição": ""
    },
    {
        "nome": "Lynn",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Frances",
        "sobrenome": "Keller",
        "descrição": ""
    },
    {
        "nome": "Barbara",
        "sobrenome": "Easley",
        "descrição": ""
    },
    {
        "nome": "Shafi",
        "sobrenome": "Hamilton",
        "descrição": ""
    },
    {
        "nome": "Dorothy",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Sister Mary",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Annie",
        "sobrenome": "Koller",
        "descrição": ""
    },
    {
        "nome": "Margaret",
        "sobrenome": "Katabi",
        "descrição": ""
    },
    {
        "nome": "Lynn",
        "sobrenome": "Gebru",
        "descrição": ""
    },
    {
        "nome": "Adele",
        "sobrenome": "Lynch",
        "descrição": ""
    },
    {
        "nome": "Fei-Fei",
        "sobrenome": "Widom",
        "descrição": ""
    },
    {
        "nome": "Daphne",
        "sobrenome": "Seneff",
        "descrição": ""
    },
    {
        "nome": "Dina",
        "sobrenome": "Sieckenius",
        "descrição": ""
    },
    {
        "nome": "Timnit",
        "sobrenome": "Asakawa",
        "descrição": ""
    },
    {
        "nome": "Nancy",
        "sobrenome": "Denton",
        "descrição": ""
    },
    {
        "nome": "Jennifer",
        "sobrenome": "Greif",
        "descrição": ""
    },
    {
        "nome": "Stephanie",
        "sobrenome": "Irwin",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Norris-Grey",
        "descrição": ""
    },
    {
        "nome": "Chieko",
        "sobrenome": "Bryant",
        "descrição": ""
    },
    {
        "nome": "Denice",
        "sobrenome": "Klawe",
        "descrição": ""
    },
    {
        "nome": "Mary Jane",
        "sobrenome": "Saujani",
        "descrição": ""
    },
    {
        "nome": "Irene",
        "sobrenome": "Borg",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Clark",
        "descrição": ""
    },
    {
        "nome": "Trudy",
        "sobrenome": "Wilkes",
        "descrição": ""
    },
    {
        "nome": "Kimberly",
        "sobrenome": "Lamarr",
        "descrição": ""
    },
    {
        "nome": "Maria",
        "sobrenome": "Perlman",
        "descrição": ""
    },
    {
        "nome": "Reshma",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Anita",
        "sobrenome": "Allen",
        "descrição": ""
    },
    {
        "nome": "Joan",
        "sobrenome": "Liskov",
        "descrição": ""
    },
    {
        "nome": "Mary",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Hedy",
        "sobrenome": "Keller",
        "descrição": ""
    },
        {
        "nome": "Barbara",
        "sobrenome": "Easley",
        "descrição": ""
    },
    {
        "nome": "Radia",
        "sobrenome": "Hamilton",
        "descrição": ""
    },
    {
        "nome": "Lynn",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Frances",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Barbara",
        "sobrenome": "Koller",
        "descrição": ""
    },
    {
        "nome": "Shafi",
        "sobrenome": "Katabi",
        "descrição": ""
    },
    {
        "nome": "Dorothy",
        "sobrenome": "Gebru",
        "descrição": ""
    },
    {
        "nome": "Sister Mary",
        "sobrenome": "Lynch",
        "descrição": ""
    },
    {
        "nome": "Annie",
        "sobrenome": "Widom",
        "descrição": ""
    },
    {
        "nome": "Margaret",
        "sobrenome": "Seneff",
        "descrição": ""
    },
    {
        "nome": "Lynn",
        "sobrenome": "Sieckenius",
        "descrição": ""
    },
    {
        "nome": "Adele",
        "sobrenome": "Asakawa",
        "descrição": ""
    },
    {
        "nome": "Fei-Fei",
        "sobrenome": "Denton",
        "descrição": ""
    },
    {
        "nome": "Daphne",
        "sobrenome": "Greif",
        "descrição": ""
    },
    {
        "nome": "Dina",
        "sobrenome": "Irwin",
        "descrição": ""
    },
    {
        "nome": "Timnit",
        "sobrenome": "Norris-Grey",
        "descrição": ""
    },
    {
        "nome": "Nancy",
        "sobrenome": "Bryant",
        "descrição": ""
    },
    {
        "nome": "Jennifer",
        "sobrenome": "Klawe",
        "descrição": ""
    },
    {
        "nome": "Stephanie",
        "sobrenome": "Saujani",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Borg",
        "descrição": ""
    },
    {
        "nome": "Chieko",
        "sobrenome": "Clark",
        "descrição": ""
    },
    {
        "nome": "Denice",
        "sobrenome": "Wilkes",
        "descrição": ""
    },
    {
        "nome": "Mary Jane",
        "sobrenome": "Lamarr",
        "descrição": ""
    },
    {
        "nome": "Irene",
        "sobrenome": "Perlman",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Trudy",
        "sobrenome": "Allen",
        "descrição": ""
    },
    {
        "nome": "Kimberly",
        "sobrenome": "Liskov",
        "descrição": ""
    },
    {
        "nome": "Maria",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Reshma",
        "sobrenome": "Keller",
        "descrição": ""
    },
    {
        "nome": "Anita",
        "sobrenome": "Easley",
        "descrição": ""
    },
    {
        "nome": "Joan",
        "sobrenome": "Hamilton",
        "descrição": ""
    },
    {
        "nome": "Mary",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Hedy",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Barbara",
        "sobrenome": "Koller",
        "descrição": ""
    },
    {
        "nome": "Radia",
        "sobrenome": "Katabi",
        "descrição": ""
    },
    {
        "nome": "Lynn",
        "sobrenome": "Gebru",
        "descrição": ""
    },
    {
        "nome": "Frances",
        "sobrenome": "Lynch",
        "descrição": ""
    },
    {
        "nome": "Barbara",
        "sobrenome": "Widom",
        "descrição": ""
    },
    {
        "nome": "Shafi",
        "sobrenome": "Seneff",
        "descrição": ""
    },
    {
        "nome": "Dorothy",
        "sobrenome": "Sieckenius",
        "descrição": ""
    },
    {
        "nome": "Sister Mary",
        "sobrenome": "Asakawa",
        "descrição": ""
    },
    {
        "nome": "Annie",
        "sobrenome": "Denton",
        "descrição": ""
    },
    {
        "nome": "Margaret",
        "sobrenome": "Greif",
        "descrição": ""
    },
    {
        "nome": "Lynn",
        "sobrenome": "Irwin",
        "descrição": ""
    },
    {
        "nome": "Adele",
        "sobrenome": "Norris-Grey",
        "descrição": ""
    },
    {
        "nome": "Fei-Fei",
        "sobrenome": "Bryant",
        "descrição": ""
    },
    {
        "nome": "Daphne",
        "sobrenome": "Klawe",
        "descrição": ""
    },
        {
        "nome": "Dina",
        "sobrenome": "Saujani",
        "descrição": ""
    },
    {
        "nome": "Timnit",
        "sobrenome": "Borg",
        "descrição": ""
    },
    {
        "nome": "Nancy",
        "sobrenome": "Clark",
        "descrição": ""
    },
    {
        "nome": "Jennifer",
        "sobrenome": "Wilkes",
        "descrição": ""
    },
    {
        "nome": "Stephanie",
        "sobrenome": "Lamarr",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Perlman",
        "descrição": ""
    },
    {
        "nome": "Chieko",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Denice",
        "sobrenome": "Allen",
        "descrição": ""
    },
    {
        "nome": "Mary Jane",
        "sobrenome": "Liskov",
        "descrição": ""
    },
    {
        "nome": "Irene",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Keller",
        "descrição": ""
    },
    {
        "nome": "Trudy",
        "sobrenome": "Easley",
        "descrição": ""
    },
    {
        "nome": "Kimberly",
        "sobrenome": "Hamilton",
        "descrição": ""
    },
    {
        "nome": "Maria",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Reshma",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Anita",
        "sobrenome": "Koller",
        "descrição": ""
    },
    {
        "nome": "Joan",
        "sobrenome": "Katabi",
        "descrição": ""
    },
    {
        "nome": "Mary",
        "sobrenome": "Gebru",
        "descrição": ""
    },
    {
        "nome": "Hedy",
        "sobrenome": "Lynch",
        "descrição": ""
    },
    {
        "nome": "Barbara",
        "sobrenome": "Widom",
        "descrição": ""
    },
    {
        "nome": "Radia",
        "sobrenome": "Seneff",
        "descrição": ""
    },
    {
        "nome": "Lynn",
        "sobrenome": "Sieckenius",
        "descrição": ""
    },
    {
        "nome": "Frances",
        "sobrenome": "Asakawa",
        "descrição": ""
    },
    {
        "nome": "Barbara",
        "sobrenome": "Denton",
        "descrição": ""
    },
    {
        "nome": "Shafi",
        "sobrenome": "Greif",
        "descrição": ""
    },
    {
        "nome": "Dorothy",
        "sobrenome": "Irwin",
        "descrição": ""
    },
    {
        "nome": "Sister Mary",
        "sobrenome": "Norris-Grey",
        "descrição": ""
    },
    {
        "nome": "Annie",
        "sobrenome": "Bryant",
        "descrição": ""
    },
    {
        "nome": "Margaret",
        "sobrenome": "Klawe",
        "descrição": ""
    },
    {
        "nome": "Lynn",
        "sobrenome": "Saujani",
        "descrição": ""
    },
    {
        "nome": "Adele",
        "sobrenome": "Borg",
        "descrição": ""
    },
    {
        "nome": "Fei-Fei",
        "sobrenome": "Clark",
        "descrição": ""
    },
    {
        "nome": "Daphne",
        "sobrenome": "Wilkes",
        "descrição": ""
    },
    {
        "nome": "Dina",
        "sobrenome": "Lamarr",
        "descrição": ""
    },
    {
        "nome": "Timnit",
        "sobrenome": "Perlman",
        "descrição": ""
    },
    {
        "nome": "Nancy",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Jennifer",
        "sobrenome": "Allen",
        "descrição": ""
    },
    {
        "nome": "Stephanie",
        "sobrenome": "Liskov",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Chieko",
        "sobrenome": "Keller",
        "descrição": ""
    },
    {
        "nome": "Denice",
        "sobrenome": "Easley",
        "descrição": ""
    },
    {
        "nome": "Mary Jane",
        "sobrenome": "Hamilton",
        "descrição": ""
    },
    {
        "nome": "Irene",
        "sobrenome": "Conway",
        "descrição": ""
    },
    {
        "nome": "Clarisse",
        "sobrenome": "Goldwasser",
        "descrição": ""
    },
    {
        "nome": "Trudy",
        "sobrenome": "Koller",
        "descrição": ""
    },
    {
        "nome": "Kimberly",
        "sobrenome": "Katabi",
        "descrição": ""
    },
    {
        "nome": "Maria",
        "sobrenome": "Gebru",
        "descrição": ""
    },
    {
        "nome": "Reshma",
        "sobrenome": "Lynch",
        "descrição": ""
    },
    {
        "nome": "Anita",
        "sobrenome": "Widom",
        "descrição": ""
    },
    {
        "nome": "Joan",
        "sobrenome": "Seneff",
        "descrição": ""
    },
    {
        "nome": "Mary",
        "sobrenome": "Sieckenius",
        "descrição": ""
    },
    {
        "nome": "Hedy",
        "sobrenome": "Asakawa",
        "descrição": ""
    }
]

nomes_completos = [f"{d['nome']} {d['sobrenome']}" for d in divas]

with open("divas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    for nome in nomes_completos:
        escritor.writerow([nome])