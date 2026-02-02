// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract VERDICTAnchor {
    event VerdictConfirmed(bytes32 verdictHash);

    function confirm(bytes32 verdictHash) external {
        emit VerdictConfirmed(verdictHash);
    }
}
