import show as sh
import test_1_palidrom as test1
import test_2_fibonacci as test2
import test_3_count_vowels as test3
import test_4_calculate_discount as test4
import test_5_flatten_list as test5
import test_6_word_frequencies as test6
import test_7_is_prime as test7

# testy palidromów
# print("Czy słowo python jest palindromem? ")
sh.Show(test1.Is_palidrome("kajak"))
sh.Show(test1.Is_palidrome("Kobyła ma mały bok"))
sh.Show(test1.Is_palidrome("python"))
sh.Show(test1.Is_palidrome(""))
sh.Show(test1.Is_palidrome("A"))

# test ciągu fibonacciego
# print("Fibonacci dla -1")
# sh.Show(test2.Fibonnaci(0))
# sh.Show(test2.Fibonnaci(1))
# sh.Show(test2.Fibonnaci(5))
# sh.Show(test2.Fibonnaci(10))
# sh.Show(test2.Fibonnaci(-1))

# test zliczanie samogłosek w tekście
# print("Zliczanie samogłosek dla słowa próba żółwia")
# sh.Show(test3.Count_vowels("Python"))
# sh.Show(test3.Count_vowels("AEIOUY"))
# sh.Show(test3.Count_vowels("bcd"))
# sh.Show(test3.Count_vowels(""))
# sh.Show(test3.Count_vowels("Próba żółwia"))

# test zniżkowy
# print("Cena 100 po uwzlędnieniu 150%")
# sh.Show(test4.Calculate_discount(100,0.2))
# sh.Show(test4.Calculate_discount(50,0))
# sh.Show(test4.Calculate_discount(200,1))
# sh.Show(test4.Calculate_discount(100,-0.1))
# sh.Show(test4.Calculate_discount(100,1.5))

# łączenie list
# print("Listy [1,[2,[3,[4]]]]")
# sh.Show(test5.flatten_list([1,2,3]))
# sh.Show(test5.flatten_list([1, [2,3], [4,[5]]]))
# sh.Show(test5.flatten_list([]))
# sh.Show(test5.flatten_list([[[1]]]))
# sh.Show(test5.flatten_list([1,[2,[3,[4]]]]))


# test częstotliwości występowania słów
# print("Ile słów powtarza się w Ala ma kota, a kot ma Ale")
# sh.Show(test6.word_frequencies("To be or not to be"))
# sh.Show(test6.word_frequencies("Hello, hello!"))
# sh.Show(test6.word_frequencies(""))
# sh.Show(test6.word_frequencies("Python Python python"))
# sh.Show(test6.word_frequencies("Ala ma kota, a kot ma Ale"))

# test liczb pierwszych
# print("Czy liczba 2 jest liczbą pierwszą")
# sh.Show(test7.Is_prime(2))
# print("Czy liczba 3 jest liczbą pierwszą")
# sh.Show(test7.Is_prime(3))
# print("Czy liczba 4 jest liczbą pierwszą")
# sh.Show(test7.Is_prime(4))
# print("Czy liczba 0 jest liczbą pierwszą")
# sh.Show(test7.Is_prime(0))
# print("Czy liczba 1 jest liczbą pierwszą")
# sh.Show(test7.Is_prime(1))
# print("Czy liczba 5 jest liczbą pierwszą")
# sh.Show(test7.Is_prime(5))
# print("Czy liczba 97 jest liczbą pierwszą")
# sh.Show(test7.Is_prime(97))
