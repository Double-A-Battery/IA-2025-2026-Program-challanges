const randomNumbers = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100));
console.log("Unsorted array:", randomNumbers);

function bubbleSort(arr) {
    let n = arr.length;
    let swapped;
    do {
        swapped = false;
        for (let i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]]; 
                swapped = true;
            }
        }
        n--;
    } while (swapped);
    return arr;
}

const sortedNumbers = bubbleSort(randomNumbers);
console.log("Sorted array:", sortedNumbers);
