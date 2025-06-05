import csv

def analyze_plant_tests(filename):
    passed = 0
    failed = 0

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            result = row['Result'].strip().lower()
            if result == 'pass':
                passed += 1
            elif result == 'fail':
                failed += 1
    
    print("Plant Test Summary Report")
    print(f"Total Passed: {passed}")
    print(f"Total Failed: {failed}")


if __name__ == '__main__':
    analyze_plant_tests('plant_tests.csv')