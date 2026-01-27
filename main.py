# create the dictonary of inventery and name ,caste, total revenue 
def main():
    dictinory_movies={
        "Inception": {"caste": ["Leonardo", "Joseph", "Page"], "total_revenue": 829895144},
        "The Dark Knight": {"caste": ["Christian", "Heath", "Aaron"], "total_revenue": 1004558444},
        "Interstellar": {"caste": ["Matthew", "Anne", "Jessica"], "total_revenue": 677471339}
    }
    # print(dictinory_movies["Inception"])
    # make the proper output
    str=input("Enter the movie name (Inception, The Dark Knight, Interstellar): ") 
    print(f"movie name is {str} caste is {dictinory_movies[str]['caste']} total revenue is {dictinory_movies[str]['total_revenue']}") 

if __name__ == "__main__":
    main()