const res = document.getElementById("res");
 let operand1 = operator = operand2 = '';
 function add(value) {
     if(operator) {
         operand2 += value;
     } else {
         operand1 += value;
     }
     renderResult();
 }
 function clearresult() {
     operand1 = operator = operand2 = '';
     renderResult();
 }
 function equal() {
     operand1 = parseInt(operand1, 2);
     operand2 = parseInt(operand2, 2);
     switch(operator) {
         case '+':
             operand1 += operand2;
             break;
         case '-':
             operand1 -= operand2;
             break;
         case '*':
             operand1 *= operand2;
             break;
         case '/':
             if(operand2)
                 operand1 /= operand2;
             break;
         default:
             break;
     }
     operand1 = parseInt(operand1).toString(2);
     operator = operand2 = '';
     renderResult();
 }
 function assignOperator(value) {
     operator = value;
     renderResult();
 }
 function renderResult() {
     res.innerHTML = operand1 + operator + operand2;
 }  