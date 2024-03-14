def calculate_people_in_row(row):
    if row == 1:
        return 1
    else:
        return row + calculate_people_in_row(row - 1)

def build_human_pyramid(rows):
    def build_row(row):
        if row == 0:
            return []
        else:
            return [build_row(row - 1)] + [calculate_people_in_row(row)]

    pyramid = build_row(rows)
    return pyramid

rows = 5
pyramid = build_human_pyramid(rows)
for row in pyramid:
    print(row)
