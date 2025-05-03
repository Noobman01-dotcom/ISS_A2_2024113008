// Write answers for q4 here
// Use the sample_analytics database
use sample_analytics;

// a. Insert one record into the accounts collection
db.accounts.insertOne({
    account_id: "ACC1001",
    limit: 5000,
    products: ["InvestmentFund", "CreditCard"]
});

// b. Insert five records into the customers collection in a single query
db.customers.insertMany([
    {
        username: "john_doe",
        name: "John Doe",
        address: { city: "New York", state: "NY", zip: "10001" },
        birthdate: ISODate("1990-04-12T00:00:00Z"),
        email: "john@example.com"
    },
    {
        username: "jane_smith",
        name: "Jane Smith",
        address: { city: "Los Angeles", state: "CA", zip: "90001" },
        birthdate: ISODate("1985-08-20T00:00:00Z"),
        email: "jane@example.com"
    },
    {
        username: "raj_kumar",
        name: "Raj Kumar",
        address: { city: "Mumbai", state: "MH", zip: "400001" },
        birthdate: ISODate("1995-12-01T00:00:00Z"),
        email: "raj@example.com"
    },
    {
        username: "li_wei",
        name: "Li Wei",
        address: { city: "Beijing", state: "BJ", zip: "100000" },
        birthdate: ISODate("1992-03-14T00:00:00Z"),
        email: "li@example.com"
    },
    {
        username: "fatima_ahmed",
        name: "Fatima Ahmed",
        address: { city: "Cairo", state: "C", zip: "11511" },
        birthdate: ISODate("1988-07-07T00:00:00Z"),
        email: "fatima@example.com"
    }
]);

// c. Multi-value search in the transactions collection
db.transactions.find({
    transaction_code: { $in: ["buy", "sell"] }
});

// d. Count the number of documents in each collection
print("Accounts count:", db.accounts.countDocuments({}));
print("Transactions count:", db.transactions.countDocuments({}));
print("Customers count:", db.customers.countDocuments({}));

// e. Update a document in the transactions collection
db.transactions.updateOne(
    { transaction_id: "TR1001" }, // Replace with an actual transaction_id if needed
    { $set: { amount: 7500, status: "processed" } }
);
