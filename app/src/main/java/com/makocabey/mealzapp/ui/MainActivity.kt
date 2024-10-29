package com.makocabey.mealzapp.ui

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.makocabey.mealzapp.ui.meals.MealsCategoriesScreen
import com.makocabey.mealzapp.ui.theme.MealzAppTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            MealzAppTheme {
                MealsCategoriesScreen()
            }
        }
    }
}

