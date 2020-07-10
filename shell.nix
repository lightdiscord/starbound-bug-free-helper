{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    (python3Packages.callPackage ./dependencies/nix-py-starbound { })
  ];
}
