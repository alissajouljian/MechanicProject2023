# CSHandwriting 
Initially, the image undergoes preprocessing involving the conversion to grayscale,
the application of blur for noise reduction, and the use of dilatation and morphological operations to highlight specific features. 
Following this, a classification process takes place based on features such as letter thickness, word distance, and the application of K-means and SVM algorithms.
Feature extraction focuses on characteristics like letter thickness and word distance. 
Among the machine learning models employed, K-means is used for clustering, while SVM emerges as the most effective classifier. 

# Stadium Billiard Simulation

This repository contains Python code to simulate the motion of a billiard ball within a stadium-shaped billiard table. The simulate_stadium_billiard function generates reflection points of the ball within the stadium, while test_stadium_billiard_generator tests the distribution of the ball's final positions across bins on the x-axis. Various parameters such as stadium width (L) and number of reflections are adjustable for experimentation. This code is useful for understanding billiard ball dynamics within non-traditional table shapes.
