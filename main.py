from openpyxl import Workbook, load_workbook

wb = load_workbook(r'C:\Users\Stalin\Documents\ggg.xlsx')
ws = wb.active
ws.title = "Data"


ws.append(['Name', 'Nationality', 'Age', 'Number', 'Race', 'Team'])
ws.append(['Giannis', 'Greek', '27', '34', 'Black', 'Bucks'])
ws.append(['Luka', 'Serbia', '23', '77', 'White', 'Mavs'])
ws.append(['Lin', 'America', '34', '7', 'Asian', 'Sharks'])
ws.append(['Hurts', 'America', '24', '1', 'Black', 'Eagles'])
ws.append(['Tua', 'Samoa', '25', '1', 'Pacific Islander', 'Dolphins'])
ws.append(['Mayfield', 'America', '27', '6', 'White', 'Panthers'])
ws.append(['Ohtani', 'Japan', '28', '17', 'Asian', 'Angels'])
ws.append(['Otamendi', 'Argentina', '34', '30', 'Hispanic', 'Benfica'])

wb.save(r'C:\Users\Stalin\Documents\ggg.xlsx')