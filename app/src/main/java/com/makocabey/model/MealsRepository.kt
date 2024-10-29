package com.makocabey.model

import com.makocabey.model.api.MealsWebService
import com.makocabey.model.response.MealsCategoriesResponse

class MealsRepository(
    private val webService: MealsWebService = MealsWebService()
) {

    suspend fun getMeals() : MealsCategoriesResponse {
        return webService.getMeals()
    }
}