const userInformation = { // Replace with your actual data retrieval method
    Nome: "John Doe",
    Email: "john.doe@example.com",
    Senha: "password123", // Consider storing passwords securely (hashed)
    Cpf: "123.456.789-00",
    Tel: "(11) 98765-4321",
    Ender: "Rua Exemplo, 123",
  };
  
  const container = document.querySelector(".d-flex"); // Replace with your container element
  
  const table = document.createElement("table");
  table.classList.add("dados-table");
  
  const tableHead = document.createElement("tr");
  const nameHeader = document.createElement("th");
  nameHeader.textContent = "Dado";
  const tableHead.appendChild(nameHeader);
  const valueHeader = document.createElement("th");
  valueHeader.textContent = "Valor";
  tableHead.appendChild(valueHeader);
  table.appendChild(tableHead);
  
  for (const key in userInformation) {
    const tableRow = document.createElement("tr");
    const nameCell = document.createElement("td");
    nameCell.textContent = key;
    tableRow.appendChild(nameCell);
    const valueCell = document.createElement("td");
    valueCell.textContent = userInformation[key];
    tableRow.appendChild(valueCell);
    table.appendChild(tableRow);
  }
  
  container.appendChild(table);