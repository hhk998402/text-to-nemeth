# text-to-nemeth

<h3>Highlights</h3>
<ul>
  <li>
    <p>Run <code>GUI.py</code> for testing the parser</p>
  </li>
  <li>
     <p>The <code>main.py</code> contains the main text2nemeth conversion function</p>
  </li>
  <li>
    <p>The <code>brl2unicode.py</code> contains the function to convert the obtained braille character to unicode for printing</p>
  </li>
  <li>
    <p>The <code>english.py</code> contains the dictionary(s) of relevant english alphabets and punctuations
  </li>
  <li>
    <p>The <code>nemethSystem.py</code> contains the dictionary(s) of relevant nemeth symbols and operators</p>
  </li>
</ul>
              
<h3>Mathematic Functions and Operators that are currently supported</h3>

<ul>
  <li>
    <h4>Use of Numeric Indicator</h4>
    <img src='https://github.com/hhk998402/text-to-nemeth/blob/master/SampleImages/NumericIndicator_1.png'>
    <br>
    <code>The numeric indicator is used to denote the first position of a numeral in a mathematical expression.</code>
    <p>Refer to <a href='https://github.com/hhk998402/text-to-nemeth/blob/master/ReferredDocuments/nemeth_Rules.pdf'>DOC 1</a> for more <b>(PAGE 12)</b></p>
  </li>  
  <li>
    <h4>Decimal Point Usage</h4>
    <img src='https://github.com/hhk998402/text-to-nemeth/blob/master/SampleImages/DecimalPoint_1.png'>
    <br>
  <code>The decimal point usage is different based on its usage. The <b>above</b> image has an example where a number exists on either side of the decimal point. The usage of the numeric indicator is different in the <b>above</b> and <b>below</b> images.</code>
    <br>
    <img src='https://github.com/hhk998402/text-to-nemeth/blob/master/SampleImages/DecimalPoint_2.png'>   
    <p>Refer to <a href='https://github.com/hhk998402/text-to-nemeth/blob/master/ReferredDocuments/nemeth_Rules.pdf'>DOC 1</a> for more <b>(PAGE 11,14)</b></p>
  </li>   
  <li>
    <h4>Multiplication Cross Operator</h4>
    <img src='https://github.com/hhk998402/text-to-nemeth/blob/master/SampleImages/MultiplicationExample.png'>
    <br>
    <code>In the code however, the * (asterisk) has been used to denote the Multiplication Cross Operator, instead of the 'x' operator </code>
    <p>Refer to <a href='https://github.com/hhk998402/text-to-nemeth/blob/master/ReferredDocuments/Nemeth-BrailleHandbookEdnaLaudenslager.pdf'>DOC 2</a> for more <b>(PAGE 75)</b></p>
  </li>  
  <li>
    <h4>Use of Superscript Indicator</h4>
    <img src='https://github.com/hhk998402/text-to-nemeth/blob/master/SampleImages/SuperscriptIndicator.png'>
    <br>
    <code>The '^' operator is used in the code to denote Superscript Indicator. Also, the Numeric Indicator seems to be ignored for exponents, and the same convention has been followed in the code</code>
    <p>Refer to <a href='https://github.com/hhk998402/text-to-nemeth/blob/master/ReferredDocuments/Nemeth-BrailleHandbookEdnaLaudenslager.pdf'>DOC 2</a> for more <b>(PAGE 100)</b></p>
  </li>
  <li>
    <h4>Use of Mathematical Comma</h4>
    <img src='https://github.com/hhk998402/text-to-nemeth/blob/master/SampleImages/MathematicalComma.png'>
    <br>
    <code>The comma used in between numbers is unique to the english usage of the comma. Both have been addressed in the code.</code>
    <p>Refer to <a href='https://github.com/hhk998402/text-to-nemeth/blob/master/ReferredDocuments/Nemeth-BrailleHandbookEdnaLaudenslager.pdf'>DOC 2</a> for more <b>(PAGE 27)</b></p>
  </li>  
</ul>
