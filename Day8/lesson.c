/*
Bonus Day 8: AI/ML Engineering Fundamentals
C Lesson: Basic Data Handling for ML

In ML, C is useful for performance-critical tasks like matrix operations.
This example shows basic array handling, which could preprocess data.

Compile: gcc lesson.c -o lesson
Run: ./lesson
*/

#include <stdio.h>
#include <stdlib.h>

// Simple struct for a "feature vector" (e.g., house features)
typedef struct {
    double size_sqft;
    int rooms;
    double price_k;  // Target
} House;

// Function to compute mean (basic stat for data analysis)
double compute_mean(double arr[], int n) {
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum / n;
}

int main() {
    // Sample data: 3 houses
    House houses[3] = {
        {1500.0, 2, 200.0},
        {2500.0, 4, 350.0},
        {1800.0, 3, 280.0}
    };

    printf("Sample House Data:\n");
    for (int i = 0; i < 3; i++) {
        printf("House %d: %.0f sq ft, %d rooms, $%.0fK\n",
               i+1, houses[i].size_sqft, houses[i].rooms, houses[i].price_k);
    }

    // Extract prices for mean calculation
    double prices[3];
    for (int i = 0; i < 3; i++) {
        prices[i] = houses[i].price_k;
    }

    double avg_price = compute_mean(prices, 3);
    printf("\nAverage Price: $%.2fK\n", avg_price);

    // In real ML, you'd use libraries like BLAS for matrix ops
    // This is just a foundation—pair with Python for full ML!

    return 0;
}

// Exercises:
// 1. Add more houses and compute variance.
// 2. Implement a simple linear prediction (manual calculation).
// 3. Integrate with Python via C extensions for speed.
