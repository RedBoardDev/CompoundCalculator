
const refreshButton = document.getElementById('refresh-button');
const calculateButton = document.getElementById('calculate-button');
const resultField = document.getElementById('result');
const result1Field = document.getElementById('result1');

refreshButton.addEventListener('click', function() {
    resultField.value = '';
    result1Field.value = '';
});

calculateButton.addEventListener('click', function() {
    const APR = document.getElementById('percentage').value;
    const gasCost = document.getElementById('number1').value;
    const initialInvestment = document.getElementById('number2').value;

    const optimumCompoundDays = calculateOptimumCompoundTime(gasCost, APR, initialInvestment);
    const optimumNbrsOfPeriods = calculateNbrsOfPeriods(optimumCompoundDays);
    const optimumGrossRewards = calculateGrossRewards(optimumNbrsOfPeriods, gasCost, APR, initialInvestment);
    result1Field.value = convertOptiTime(optimumCompoundDays);
    resultField.value = round(((optimumGrossRewards / initialInvestment) * 100), 2) + '%';
});
