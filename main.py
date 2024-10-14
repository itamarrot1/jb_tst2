import unittest

def run_tests():
    # Discover and run all tests in the 'test' directory
    loader = unittest.TestLoader()
    suite = loader.discover('test')  # Ensure 'test' is the correct directory for your test modules

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Print the results summary
    print("\nTest Summary:")
    print("--------------")
    print(f"Total tests run: {result.testsRun}")

    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print(f"Tests failed: {len(result.failures) + len(result.errors)}")
        for failed_test, traceback in result.failures:
            print(f"Failure: {failed_test} - {traceback}")
        for error_test, traceback in result.errors:
            print(f"Error: {error_test} - {traceback}")

if __name__ == '__main__':
    run_tests()
