<p align="center">
  <img src="https://i.imgur.com/5VacA1K.png" width="150"/>
  <h1 align="center">FixedFloat API - Python</h1>
  <p align="center">
    <br>FixedFloat API - Python (unofficial)
    <br><a href="https://fixedfloat.com/?ref=a7u3rzvc">Get API Key</a> | <a href="https://fixedfloat.com/api">Docs</a> | <a href="https://fixedfloat.com/">Website</a> | <a href="https://fixedfloat.com/faq">FAQ</a>
  </p>
</p>

## Installation
Manual
```bash
git clone https://github.com/GFXFischer/fixedfloat_api.git
pip install -r requirements.txt
```


## Usage
```python
from fixedfloat_api import FixedFloat
fixedfloat_api = FixedFloat("API_KEY", "SECRET_KEY")

```

## Methods

* [.getCurrencies()](#getcurrencies)
* [.getPrice(fromCurrency, toCurrency, fromQty, toQty, type)](#getpricefromcurrency-tocurrency-fromqty-toqty-type)
* [.getOrder(id, token)](#getorderid-token)
* [.setEmergency(id, token, choice, address)](#setemergencyid-token-choice-address)
* [.createOrder(fromCurrency, toCurrency, toAddress, fromQty, toQty, type, extra)](#createorderfromcurrency-tocurrency-toaddress-fromqty-toqty-type-extra)

### .getCurrencies()

Getting a list of all currencies that are available. [Official docs](https://fixedfloat.com/api#method_getCurrencies)

```python
response = fixedfloat_api.getCurrencies()
```

### .getPrice(fromCurrency, toCurrency, fromQty, toQty, type)

Information about a currency pair with a set amount of funds. [Official docs](https://fixedfloat.com/api#method_getPrice)

```python
// Fixed
response = fixedfloat_api.getPrice("USDCBSC", "BTC", 25.00, type="fixed")

// Float
response = fixedfloat_api.getPrice("USDCBSC", "BTC", 25.00)
```

### .getOrder(id, token)

Receiving information about the order. [Official docs](https://fixedfloat.com/api#method_getOrder)
```python
response = fixedfloat_api.getOrder("ID", "TOKEN")
```

### .setEmergency(id, token, choice, address)

Emergency Action Choice. [Official docs](https://fixedfloat.com/api#method_setEmergency)

```python
// Exchange
response = fixedfloat_api.setEmergency("ID", "TOKEN", "EXCHANGE")

// Refund
response = fixedfloat_api.setEmergency("ID", "TOKEN", "REFUND", "ADDRESS")
```

### .createOrder(fromCurrency, toCurrency, toAddress, fromQty, toQty, type, extra)

Creating exchange order. [Official docs](https://fixedfloat.com/api#method_createOrder)

```python
// Fixed
response = fixedfloat_api.createOrder("USDCBSC", "BTC", "ADDRESS", 25.00, type="fixed")

// Float
response = fixedfloat_api.createOrder("USDCBSC", "BTC", "ADDRESS", 25.00)
```

## License
fixedfloat_api is Licensed under the [MIT License](https://github.com/GFXFischer/fixedfloat_api/blob/main/LICENSE)
