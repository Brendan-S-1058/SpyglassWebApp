
document.addEventListener("DOMContentLoaded", function () {
    const idsToReplace = [
        "AutoFuel", "Feed", "TeleFuel", "Missed"
    ];

    idsToReplace.forEach(id => {
        let inputField = document.getElementById(id);
        if (inputField) {
            let wrapper = document.createElement("div");
            wrapper.style.display = "flex";
            wrapper.style.alignItems = "center";
            wrapper.style.gap = "5px";

            let minusButton = document.createElement("button");
            minusButton.textContent = "-";
            minusButton.type = "button";
            minusButton.style.padding = "5px 10px";

            let numberInput = document.createElement("input");
            numberInput.type = "number";
            numberInput.id = id;
            numberInput.name = id;
            numberInput.value = 0;
            numberInput.style.width = "50px";
            numberInput.style.textAlign = "center";

            let plusButton = document.createElement("button");
            plusButton.textContent = "+";
            plusButton.type = "button";
            plusButton.style.padding = "5px 10px";

            minusButton.addEventListener("click", () => {
                numberInput.value = Math.max(0, parseInt(numberInput.value) - 1);
            });

            plusButton.addEventListener("click", () => {
                numberInput.value = parseInt(numberInput.value) + 1;
            });

            wrapper.appendChild(minusButton);
            wrapper.appendChild(numberInput);
            wrapper.appendChild(plusButton);

            inputField.parentNode.replaceChild(wrapper, inputField);
        }
    });
});