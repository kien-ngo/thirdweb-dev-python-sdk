"""Generated wrapper for ILazyMintWithTier Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for ILazyMintWithTier below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ILazyMintWithTierValidator,
    )
except ImportError:

    class ILazyMintWithTierValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class LazyMintMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the lazyMint method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        extra_data: Union[bytes, str],
    ):
        """Validate the inputs to the lazyMint method."""
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="amount",
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="baseURIForTokens",
            argument_value=base_uri_for_tokens,
        )
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="tier",
            argument_value=tier,
        )
        self.validator.assert_valid(
            method_name="lazyMint",
            parameter_name="extraData",
            argument_value=extra_data,
        )
        return (amount, base_uri_for_tokens, tier, extra_data)

    def call(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        extra_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            amount,
            base_uri_for_tokens,
            tier,
            extra_data,
        ) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens, tier, extra_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(
            amount, base_uri_for_tokens, tier, extra_data
        ).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        extra_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            amount,
            base_uri_for_tokens,
            tier,
            extra_data,
        ) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens, tier, extra_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            amount, base_uri_for_tokens, tier, extra_data
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        extra_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            amount,
            base_uri_for_tokens,
            tier,
            extra_data,
        ) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens, tier, extra_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            amount, base_uri_for_tokens, tier, extra_data
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        amount: int,
        base_uri_for_tokens: str,
        tier: str,
        extra_data: Union[bytes, str],
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            amount,
            base_uri_for_tokens,
            tier,
            extra_data,
        ) = self.validate_and_normalize_inputs(
            amount, base_uri_for_tokens, tier, extra_data
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            amount, base_uri_for_tokens, tier, extra_data
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ILazyMintWithTier:
    """Wrapper class for ILazyMintWithTier Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """

    lazy_mint: LazyMintMethod
    """Constructor-initialized instance of
    :class:`LazyMintMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ILazyMintWithTierValidator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param web3_or_provider: Either an instance of `web3.Web3`:code: or
            `web3.providers.base.BaseProvider`:code:
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = ILazyMintWithTierValidator(
                web3_or_provider, contract_address
            )

        web3 = None
        if isinstance(web3_or_provider, BaseProvider):
            web3 = Web3(web3_or_provider)
        elif isinstance(web3_or_provider, Web3):
            web3 = web3_or_provider
        else:
            raise TypeError(
                "Expected parameter 'web3_or_provider' to be an instance of either"
                + " Web3 or BaseProvider"
            )

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                        middleware["function"],
                        layer=middleware["layer"],
                    )
            except ValueError as value_error:
                if value_error.args == (
                    "You can't add the same un-named instance twice",
                ):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address),
            abi=ILazyMintWithTier.abi(),
        ).functions

        self.lazy_mint = LazyMintMethod(
            web3_or_provider, contract_address, functions.lazyMint, validator
        )

    def get_tokens_lazy_minted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensLazyMinted event.

        :param tx_hash: hash of transaction emitting TokensLazyMinted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=ILazyMintWithTier.abi(),
            )
            .events.TokensLazyMinted()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"string","name":"tier","type":"string"},{"indexed":true,"internalType":"uint256","name":"startTokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endTokenId","type":"uint256"},{"indexed":false,"internalType":"string","name":"baseURI","type":"string"},{"indexed":false,"internalType":"bytes","name":"encryptedBaseURI","type":"bytes"}],"name":"TokensLazyMinted","type":"event"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"string","name":"baseURIForTokens","type":"string"},{"internalType":"string","name":"tier","type":"string"},{"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"lazyMint","outputs":[{"internalType":"uint256","name":"batchId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
