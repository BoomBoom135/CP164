"""
-------------------------------------------------------
Array version of the set ADT.
-------------------------------------------------------
Author: Nick Shahbaz Sayyad Shahbaz
ID:     169063423
Email:  sayy3423@mylaurier.ca
__updated__ = "2024-02-28"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty set.
        Use: source = Set()
        -------------------------------------------------------
            Creates a new Set object. (Set)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            True if source is empty, False otherwise. (boolean)
        -------------------------------------------------------
        """
        # your code here
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            the number of values in source. (int)
        -------------------------------------------------------
        """
        # your code here
        return len(self._values)

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Private helper method.
        -------------------------------------------------------
        Returns the index of key in a Set, -1 if key is not found.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            i - the index of key in the Set, -1 otherwise. (int)
        -------------------------------------------------------
        """
        # your code here
        if not self.is_empty():
            i = 0
            while i < len(self._values) and self._values[i] != key:
                i += 1
            if i == len(self._values):
                i = -1
        else:
            i = -1
        return i

    def append(self, value):
        """
        -------------------------------------------------------
        If value does not already exist in source, appends a copy of value
        to source. Returns True if value is appended, False otherwise.
        Use: appended = source.append(value)
        -------------------------------------------------------
        Parameters:
            value - data. (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            appended - True if value appended to source, False otherwise. (boolean)
        -------------------------------------------------------
        """
        i = self._linear_search(value)

        if i == -1:
            self._values.append(deepcopy(value))
            appended = True
        else:
            # value already in set
            appended = False

        return appended

    def discard(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source that matches key.
        Returns None if key not in source.
        Use: value = source.discard(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            value - the full value matching key, None otherwise. (*)
        -------------------------------------------------------
        """
        # your code here
        if not self.is_empty():
            i = 0
            while i < len(self._values) and self._values[i] != key:
                i += 1
            if i == len(self._values):
                value = None
            else:
                value = self._values.pop(i)
        else:
            value = None

        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Returns True if source contains key, False otherwise.
        Use: contains = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            True if source contains key, False otherwise. (boolean)Priority_Queue
        -------------------------------------------------------
        """
        # your code here
        if not self.is_empty():
            i = 0
            while i < len(self._values) and self._values[i] != key:
                i += 1
            if i == len(self._values):
                contains = False
            else:
                contains = True
        else:
            contains = False

        return contains

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            value - a copy of the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """
        # your code here
        if not self.is_empty():
            i = 0
            while i < len(self._values) and self._values[i] != key:
                i += 1
            if i == len(self._values):
                value = None
            else:
                value = deepcopy(self._values[i])
        else:
            value = None

        return value

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether source == target.
        If source and target are of the same length and contain the same values,
        returns True, otherwise returns False.
        Order is not significant.
        Use: equals = source == target
        -------------------------------------------------------
        Parameters:
            target - another set (Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            equals - True if source contains the same values as target,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3} == {1,2,3}: True
            {1,2,3} == {3,1,2}: True
            {1,2,3,5} == {4,3,1,2}: False
        -------------------------------------------------------
        """
        # your code here
        if len(self._values) == len(target._values):
            i = 0
            while i < len(self._values) and self._values[i] in target._values:
                i += 1
            if i == len(self._values):
                equals = True
            else:
                equals = False
        else:
            equals = False

        return equals

    def issubset(self, target):
        """
        ---------------------------------------------------------
        Test whether every element in source is also in target.
        Order is not significant.
        Use: subset = source.issubset(target)
        -------------------------------------------------------
        Parameters:
            target - another set. (Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            subset - True if all values in source are also in target,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issubset({4,2,1,3,0}: True
            {1,2,3}.issubset({1,2,3}): True
            {1,2,3}.issubset({1,3,4}): False
        -------------------------------------------------------
        """
        # your code here
        subset = True
        for i in self._values:
            if i not in target._values:
                subset = False

        return subset

    def issuperset(self, target):
        """
        ---------------------------------------------------------
        Test whether every value in target is also in source.
        Use: superset = source.issuperset(target)
        -------------------------------------------------------
        Parameters:
            target - another Set. (Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌‌​​‌‌‌​‌​​‌​:
            superset - True if all values in target are also in source,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issuperset({0,1,2,3,4}): False
            {1,2,3,4,5}.issuperset({1,2,4,5}): True
        -------------------------------------------------------
        """
        # your code here
        superset = True
        for i in target._values:
            if i not in self._values:
                superset = False

        return superset

    def isdisjoint(self, target):
        """
        -------------------------------------------------------
        Return True if source has no values in common with target.
        Sets are disjoint if and only if their intersection is the empty Set.
        Order is not significant.
        Use: disjoint = source.isdisjoint(target)
        -------------------------------------------------------
        Parameters:
            target - a Set to compare against source. (Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            disjoint - True if source has no values in common with target,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3}.isdisjoint({4,5,6,7}): True
            {1,2,3}.isdisjoint({4,5,6,1,7}): False
        -------------------------------------------------------
        """
        # your code here
        disjoint = True
        for i in self._values:
            if i in target._values:
                disjoint = False

        return disjoint

    def intersection(self, target):
        """
        -------------------------------------------------------
        Return a new Set with copies of values common to source and target.
        Order is not significant.
        Use: new_set = source.intersection(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based set. (Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            new_set - the intersection of source and target. (Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.intersection({4,3,5}): {3}
            {1,2,3}.intersection({5,6,0}): {}
        -------------------------------------------------------
        """
        # your code here
        new_set = Set()
        for i in self._values:
            if i in target._values:
                new_set.append(i)

        return new_set

    def union(self, target):
        """
        -------------------------------------------------------
        Return a new Set with copies of all unique values from source and target.
        Order is not significant.
        Use: new_set = source.union(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based set (Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            new_set - the union of source and target (Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.union({4,3,5}): {1,2,3,4,5}
        -------------------------------------------------------
        """
        # your code here
        new_set = Set()
        for i in self._values:
            new_set.append(i)
        for i in target._values:
            if i not in self._values:
                new_set.append(i)

        return new_set

    def difference(self, target):
        """
        -------------------------------------------------------
        Return a new Set with copies of values in source that are not in target.
        Order is not significant.
        Use: new_set = source.difference(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based Set. (Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            new_set - the difference of source and target. (Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.difference({4,3,5}): {1,2}
        -------------------------------------------------------
        """
        # your code here
        new_set = Set()
        for i in self._values:
            if i not in target._values:
                new_set.append(i)

        return new_set

    def symmetric_difference(self, target):
        """
        -------------------------------------------------------
        Return a new set with copies of values in either source or target but not both.
        Order is not significant.
        Use: new_set = source.symmetric_difference(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based Set. (Set)
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            new_set - the symmetric difference of source and target. (Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.symmetric_difference({4,3,5}): {1,2,4,5}
        -------------------------------------------------------
        """
        # your code here
        new_set = Set()
        for i in self._values:
            if i not in target._values:
                new_set.append(i)
        for i in target._values:
            if i not in self._values:
                new_set.append(i)

        return new_set

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌​‌‌​​‌‌‌‌‌‌‌‌‌‌:
            value - the next value in the Set. (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
