
# problem link-->> https://leetcode.com/problems/design-movie-rental-system/description

from sortedcontainers import SortedList
from collections import defaultdict
from typing import List

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        """
        Initialize movie rental system with SortedList data structures
        TC: O(E log E), SC: O(E) where E = number of entries
        """
        # Map: movie_id -> SortedList of (price, shop) for unrented copies
        self.unrented_movies = defaultdict(SortedList)
        
        # SortedList of (price, shop, movie) for all rented movies
        self.rented_movies = SortedList()
        
        # Quick price lookup: (shop, movie) -> price
        self.prices = {}
        
        # Initialize all movies as unrented
        for shop, movie, price in entries:
            self.unrented_movies[movie].add((price, shop))
            self.prices[(shop, movie)] = price
    
    def search(self, movie: int) -> List[int]:
        """
        Find cheapest 5 unrented shops for given movie
        TC: O(1), SC: O(1)
        """
        if movie not in self.unrented_movies:
            return []
        
        sorted_list = self.unrented_movies[movie]
        return [shop for price, shop in sorted_list[:5]]
    
    def rent(self, shop: int, movie: int) -> None:
        """
        Rent movie from shop - move from unrented to rented
        TC: O(log n), SC: O(1)
        """
        price = self.prices[(shop, movie)]
        
        # Remove from unrented movies
        self.unrented_movies[movie].remove((price, shop))
        
        # Add to rented movies (sorted by price, shop, movie)
        self.rented_movies.add((price, shop, movie))
    
    def drop(self, shop: int, movie: int) -> None:
        """
        Drop rented movie back to shop - move from rented to unrented
        TC: O(log n), SC: O(1)
        """
        price = self.prices[(shop, movie)]
        
        # Remove from rented movies
        self.rented_movies.remove((price, shop, movie))
        
        # Add back to unrented movies
        self.unrented_movies[movie].add((price, shop))
    
    def report(self) -> List[List[int]]:
        """
        Get 5 cheapest currently rented movies
        TC: O(1), SC: O(1)
        """
        return [[shop, movie] for price, shop, movie in self.rented_movies[:5]]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
