// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title VERDICTAnchor v0.2
/// @notice Execution-free finality anchor.
///         Proof-first. Ethereum is the final court.
/// @dev    This contract does NOT verify proofs.
///         Existence on-chain == responsibility off-chain.
contract VERDICTAnchor {
    /// @dev Version tag to make upgrades explicit and indexable.
    uint256 public constant VERSION = 2;

    /// @notice Emitted when a verdict is finalized with an accompanying proof hash.
    /// @param verdictHash Hash of the VerdictTable (canonical, sorted, off-chain)
    /// @param proofHash   Hash of the proof (zk-proof or stub; scheme-agnostic)
    event VerdictConfirmed(bytes32 verdictHash, bytes32 proofHash);

    /// @notice Confirm a verdict with its proof.
    /// @param verdictHash Hash of the VerdictTable
    /// @param proofHash   Hash of the proof
    /// @dev No validation is performed. The chain only anchors existence.
    function confirm(bytes32 verdictHash, bytes32 proofHash) external {
        emit VerdictConfirmed(verdictHash, proofHash);
    }
}
