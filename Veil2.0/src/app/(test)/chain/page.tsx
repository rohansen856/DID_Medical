"use client"

import { useEffect, useState } from "react"
import { useSDK } from "@metamask/sdk-react"
import { InfoIcon, WalletIcon } from "lucide-react"

import { toast } from "@/hooks/use-toast"
import { Button } from "@/components/ui/button"
import { ToastAction } from "@/components/ui/toast"
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"
import { MedicalContract } from "@/components/contract"
import MetaMaskProvider from "@/components/MetamaskProvider"

const GANACHE_TESTNET_CHAIN = "0x539" // Ganache testnet chain ID
const LOCAL_TESTNET_CHAIN = "0x7a69" // Local testnet chain ID

const switchEthereumChain = async () => {
  if (!window.ethereum) return

  try {
    await window.ethereum.request({
      method: "wallet_switchEthereumChain",
      params: [{ chainId: GANACHE_TESTNET_CHAIN }],
    })
    window.location.reload() // Reload the page to apply the chain switch
  } catch (error) {
    console.error("Failed to switch chain", error)
  }
}

export const ConnectWalletButton = () => {
  const [chainId, setChainId] = useState<string | null>(null)
  const [connected, setConnected] = useState<boolean>(false)
  const [contract, setContract] = useState<MedicalContract>()
  const { sdk, connecting, account, balance } = useSDK()

  useEffect(() => {
    if (window?.ethereum?.chainId) {
      setChainId(window.ethereum.chainId)
    }

    const checkConnection = async () => {
      if (window.ethereum && window.ethereum.selectedAddress) {
        setChainId(window.ethereum.chainId)
        setConnected(true)
      } else {
        setConnected(false)
      }
    }

    checkConnection()

    const handleAccountsChanged = (accounts: string[]) => {
      if (accounts.length > 0) {
        console.log("Account changed:", accounts[0])
        setConnected(true)
      } else {
        console.log("Disconnected from MetaMask")
        setConnected(false)
      }
    }

    const handleChainChanged = (chainId: string) => {
      setChainId(chainId)
    }

    window.ethereum?.on("accountsChanged", handleAccountsChanged)
    window.ethereum?.on("chainChanged", handleChainChanged)

    return () => {
      window.ethereum?.removeListener("accountsChanged", handleAccountsChanged)
      window.ethereum?.removeListener("chainChanged", handleChainChanged)
    }
  }, [])

  const isOnGanacheTestnet = chainId === GANACHE_TESTNET_CHAIN
  const isOnLocalTestnet = chainId === LOCAL_TESTNET_CHAIN

  const connect = async () => {
    if (!window.ethereum) return alert("Metamask not installed!")
    try {
      const accounts = await window.ethereum.request({
        method: "eth_requestAccounts",
      })
      if (accounts) {
        console.log("Public Address:", accounts[0])
        setConnected(true)
        setChainId(window.ethereum.chainId)
        window.localStorage.setItem("eth_id", accounts[0])
        toast({
          title: "Metamask Connected!",
          description: "address: " + accounts[0].slice(0, 15) + "...",
          action: (
            <ToastAction
              altText="Logout"
              onClick={disconnect}
              className="bg-destructive/50"
            >
              Logout
            </ToastAction>
          ),
        })
      } else {
        console.error("No accounts found.")
      }
    } catch (err) {
      console.warn(`Error connecting to MetaMask:`, err)
    }
  }

  const disconnect = async () => {
    await sdk?.terminate()
    window.localStorage.removeItem("eth_id")
    setConnected(false)
  }

  async function initContract() {
    if (!account) return
    const data = new MedicalContract(account)
    await data.init()
    setContract(data)
  }

  useEffect(() => {
    initContract()
  }, [account])

  return (
    <div className="relative">
      {connected ? (
        isOnGanacheTestnet || isOnLocalTestnet ? (
          <div className="flex items-center gap-4">
            <Button variant="destructive" onClick={disconnect}>
              <WalletIcon className="size-4" /> Disconnect
            </Button>

            <TooltipProvider>
              <Tooltip>
                <TooltipTrigger asChild>
                  <InfoIcon className="size-6 text-primary/50" />
                </TooltipTrigger>
                <TooltipContent>
                  <code>{balance ?? "Balance not available"}</code>
                </TooltipContent>
              </Tooltip>
              -32603
            </TooltipProvider>
          </div>
        ) : (
          <Button variant="destructive" onClick={switchEthereumChain}>
            Switch to Ganache
          </Button>
        )
      ) : (
        <Button variant="default" disabled={connecting} onClick={connect}>
          <WalletIcon className="size-4" /> Connect MetaMask
        </Button>
      )}
      <Button
        onClick={async () => {
          try {
            if (account) {
              const doc = await contract?.registerDoctor("Rohan", "Ortho", 2)
              console.log(doc)
            } else toast({ title: "No account!" })
          } catch (error) {
            if (error.code == -32603) {
              toast({
                title: "You have already registered!",
                variant: "destructive",
              })
            }
          }
        }}
      >
        Register as Doctor
      </Button>
      <Button
        onClick={async () => {
          if (account) {
            const doc = await contract?.getDoctor(account)
            console.log(doc)
          } else toast({ title: "No account!" })
        }}
      >
        Get Doctor
      </Button>
    </div>
  )
}

const ChainTestPage = () => {
  return (
    <MetaMaskProvider>
      <ConnectWalletButton />
    </MetaMaskProvider>
  )
}

export default ChainTestPage
