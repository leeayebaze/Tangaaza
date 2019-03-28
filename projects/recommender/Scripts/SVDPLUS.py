#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:16:45 2019

@author: ayebaze
"""

from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate

class SVDD():
    def svdfn(self):
        # Load the movielens-100k dataset (download it if needed).
        data = Dataset.load_builtin('ml-100k')

        # Use the famous SVD algorithm.
        algo = SVD()

        # Run 5-fold cross-validation and print results.
        cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

        return cross_validate