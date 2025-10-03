# TDD Driven StringCalculator

Build a StringCalculator functionality that can take up to two numbers, separated by commas, and will return their sum. 
for example “” or “1” or “1,2” as inputs.

> DO NOT jump into implementation! Read the example and the starting task below.

- For an empty string it will return 0
- Allow the Add method to handle an unknown amount of numbers
- Allow the Add method to handle new lines between numbers (instead of commas).
  - the following input is ok: “1\n2,3” (will equal 6)
  - the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)
- Support different delimiters : to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
the first line is optional. all existing scenarios should still be supported
- Calling Method with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. if there are multiple negatives, show all of them in the exception message.
- Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2
- Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6

## Tasks



Establish quality parameters:

- Ensure  maximum complexity (CCN) per function == 3

- Ensure 100% line and branch coverage at every step

  

Start Test-driven approach

1. Write the smallest possible failing test: give input `"" assert output to be 0 ` .
2. Write the minimum amount of code that'll make it pass.
3. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

Test Specification:

| **Test Case ID** | **Test Name**                | **Input**                    | **Expected Output / Behavior**                | **Notes**                    |
| ---------------- | ---------------------------- | ---------------------------- | --------------------------------------------- | ---------------------------- |
| TC1              | TestEmptyString              | `""`                         | `0`                                           | Empty string returns 0       |
| TC2              | TestSingleNumber             | `"1"`                        | `1`                                           | Single number                |
| TC3              | TestAnotherSingleNumber      | `"7"`                        | `7`                                           | Another single number        |
| TC4              | TestTwoNumbers               | `"1,2"`                      | `3`                                           | Two numbers, comma-separated |
| TC5              | TestTwoLargerNumbers         | `"10,20"`                    | `30`                                          | Two larger numbers           |
| TC6              | TestMultipleNumbers          | `"1,2,3,4,5"`                | `15`                                          | Unknown amount of numbers    |
| TC7              | TestFourNumbers              | `"10,20,30,40"`              | `100`                                         | Multiple numbers             |
| TC8              | TestNewlineDelimiter         | `"1\n2,3"`                   | `6`                                           | Newline as delimiter         |
| TC9              | TestInvalidDelimiterCase     | `"1,\n"`                     | Invalid (not required to handle)              | Clarification only           |
| TC10             | TestCustomDelimiterSemicolon | `"//;\n1;2"`                 | `3`                                           | Custom delimiter `;`         |
| TC11             | TestCustomDelimiterDash      | `"//-\n5-6-7"`               | `18`                                          | Custom delimiter `-`         |
| TC12             | TestNegativeNumber           | `"1,-2,3"`                   | Exception → `"negatives not allowed: -2"`     | Negative number              |
| TC13             | TestMultipleNegatives        | `"-1,-5,7"`                  | Exception → `"negatives not allowed: -1, -5"` | Multiple negatives           |
| TC14             | TestIgnoreNumbersAbove1000   | `"2,1001"`                   | `2`                                           | Ignore >1000                 |
| TC15             | TestIncludeThousand          | `"1000,2"`                   | `1002`                                        | 1000 is allowed              |
| TC16             | TestLongDelimiter            | `"//[***]\n1***2***3"`       | `6`                                           | Delimiter of any length      |
| TC17             | TestAnotherLongDelimiter     | `"//[###]\n4###5###6"`       | `15`                                          | Another long delimiter       |
| TC18             | TestMultipleDelimiters       | `"//[*][%]\n1*2%3"`          | `6`                                           | Multiple delimiters          |
| TC19             | TestMultipleLongDelimiters   | `"//[***][%%]\n10***20%%30"` | `60`                                          | Multiple long delimiters     |

