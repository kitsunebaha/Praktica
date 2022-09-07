def get_name (отделение, специальность, группа)
	full_name=f"{отделение}{специальность}{группа}"
	return full_name.title()
mic=get_name ("ФСПО", "Прикладная информатика", "ДКЕО-42")
print(mic)