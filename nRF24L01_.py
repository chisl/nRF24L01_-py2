#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""nRF24L01+: Single Chip 2.4GHz Transceiver"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Nordic Semiconductor"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

from nRF24L01__constants import *

# name:        nRF24L01+
# description: Single Chip 2.4GHz Transceiver
# manuf:       Nordic Semiconductor
# version:     0.1
# url:         https://www.nordicsemi.com/eng/content/download/2726/34069/file/nRF24L01P_Product_Specification_1_0.pdf
# date:        2017-12-19


# Derive from this class and implement read and write
class nRF24L01__Base:
	"""Single Chip 2.4GHz Transceiver"""
	# Register CONFIG
	# Configuration Register 
	
	def setCONFIG(self, val):
		"""Set register CONFIG"""
		self.write(REG.CONFIG, val, 8)
	
	def getCONFIG(self):
		"""Get register CONFIG"""
		return self.read(REG.CONFIG, 8)
	
	# Bits Reserved_0
	# Only '0' allowed 
	# Bits MASK_RX_DR
	# Mask interrupt caused by RX_DR
	#           1: Interrupt not reflected on the IRQ pin
	#           0: Reflect RX_DR as active low interrupt on the
	#           IRQ pin 
	
	# Bits MASK_TX_DS
	# Mask interrupt caused by TX_DS
	#           1: Interrupt not reflected on the IRQ pin
	#           0: Reflect TX_DS as active low interrupt on the IRQ
	#           pin 
	
	# Bits MASK_MAX_RT
	# Mask interrupt caused by MAX_RT
	#           1: Interrupt not reflected on the IRQ pin
	#           0: Reflect MAX_RT as active low interrupt on the
	#           IRQ pin 
	
	# Bits EN_CRC
	# Enable CRC. Forced high if one of the bits in the
	#           EN_AA is high 
	
	# Bits CRCO
	# CRC encoding scheme 
	# Bits PWR_UP
	# 1: POWER UP, 0:POWER DOWN 
	# Bits PRIM_RX
	# RX/TX control
	#           1: PRX, 0: PTX 
	
	# Register EN_AA
	# Enable 'Auto Acknowledgment' Function Disable
	#       this functionality to be compatible with nRF2401,
	#       see page 75 
	
	
	def setEN_AA(self, val):
		"""Set register EN_AA"""
		self.write(REG.EN_AA, val, 8)
	
	def getEN_AA(self):
		"""Get register EN_AA"""
		return self.read(REG.EN_AA, 8)
	
	# Bits Reserved_0
	# Only '00' allowed 
	# Bits ENAA_P5
	# Enable auto acknowledgement data pipe 5 
	# Bits ENAA_P4
	# Enable auto acknowledgement data pipe 4 
	# Bits ENAA_P3
	# Enable auto acknowledgement data pipe 3 
	# Bits ENAA_P2
	# Enable auto acknowledgement data pipe 2 
	# Bits ENAA_P1
	# Enable auto acknowledgement data pipe 1 
	# Bits ENAA_P0
	# Enable auto acknowledgement data pipe 0 
	# Register EN_RXADDR
	# Enabled RX Addresses 
	
	def setEN_RXADDR(self, val):
		"""Set register EN_RXADDR"""
		self.write(REG.EN_RXADDR, val, 8)
	
	def getEN_RXADDR(self):
		"""Get register EN_RXADDR"""
		return self.read(REG.EN_RXADDR, 8)
	
	# Bits Reserved_0
	# Only '00' allowed 
	# Bits ERX_P5
	# Enable data pipe 5. 
	# Bits ERX_P4
	# Enable data pipe 4. 
	# Bits ERX_P3
	# Enable data pipe 3. 
	# Bits ERX_P2
	# Enable data pipe 2. 
	# Bits ERX_P1
	# Enable data pipe 1. 
	# Bits ERX_P0
	# Enable data pipe 0. 
	# Register SETUP_AW
	# Setup of Address Widths
	#       (common for all data pipes) 
	
	
	def setSETUP_AW(self, val):
		"""Set register SETUP_AW"""
		self.write(REG.SETUP_AW, val, 8)
	
	def getSETUP_AW(self):
		"""Get register SETUP_AW"""
		return self.read(REG.SETUP_AW, 8)
	
	# Bits Reserved_0
	# Only '000000' allowed 
	# Bits AW
	# RX/TX Address field width
	#           '00' - Illegal
	#           '01' - 3 bytes
	#           '10' - 4 bytes
	#           11' - 5 bytes
	#           LSByte is used if address width is below 5 bytes 
	
	# Register SETUP_RETR
	# Setup of Automatic Retransmission 
	
	def setSETUP_RETR(self, val):
		"""Set register SETUP_RETR"""
		self.write(REG.SETUP_RETR, val, 8)
	
	def getSETUP_RETR(self):
		"""Get register SETUP_RETR"""
		return self.read(REG.SETUP_RETR, 8)
	
	# Bits ARDa
	# Auto Retransmit Delay
	#           4'b0000 Wait 250µs
	#           4'b0001 Wait 500µs
	#           4'b0010 Wait 750µs
	#           ........
	#           4b1111 Wait 4000µs
	#           (Delay defined from end of transmission to start of
	#           next transmission)b 
	
	# Bits ARC
	# Auto Retransmit Count
	#           4'b0000 Re-Transmit disabled
	#           4b0001 Up to 1 Re-Transmit on fail of AA
	#           ......
	#           4b1111 Up to 15 Re-Transmit on fail of AA 
	
	# Register RF_CH
	# RF Channel 
	
	def setRF_CH(self, val):
		"""Set register RF_CH"""
		self.write(REG.RF_CH, val, 8)
	
	def getRF_CH(self):
		"""Get register RF_CH"""
		return self.read(REG.RF_CH, 8)
	
	# Bits Reserved_0
	# Only '0' allowed 
	# Bits RF_CH
	# Sets the frequency channel nRF24L01+ operates on 
	# Register RF_SETUP
	# RF Setup Register 
	
	def setRF_SETUP(self, val):
		"""Set register RF_SETUP"""
		self.write(REG.RF_SETUP, val, 8)
	
	def getRF_SETUP(self):
		"""Get register RF_SETUP"""
		return self.read(REG.RF_SETUP, 8)
	
	# Bits CONT_WAVE
	# Enables continuous carrier transmit when high. 
	# Bits Reserved_0
	# Only '0' allowed 
	# Bits RF_DR_LOW
	# Set RF Data Rate to 250kbps. See RF_DR_HIGH
	#           for encoding. 
	
	# Bits PLL_LOCK
	# Force PLL lock signal. Only used in test 
	# Bits RF_DR_HIGH
	# Select between the high speed data rates. This bit
	#           is don't care if RF_DR_LOW is set.
	#           Encoding:
	#           [RF_DR_LOW, RF_DR_HIGH]:
	#           2'b00 - 1Mbps
	#           2'b01 - 2Mbps
	#           2'b10 - 250kbps
	#           2'b11 - Reserved 
	
	# Bits RF_PWR
	# Set RF output power in TX mode 
	# Bits Obsolete
	# Don't care
	# Register STATUS
	# Status Register (In parallel to the SPI command
	#       word applied on the MOSI pin, the STATUS register
	#       is shifted serially out on the MISO pin) 
	
	
	def setSTATUS(self, val):
		"""Set register STATUS"""
		self.write(REG.STATUS, val, 8)
	
	def getSTATUS(self):
		"""Get register STATUS"""
		return self.read(REG.STATUS, 8)
	
	# Bits Reserved_0
	# Only '0' allowed 
	# Bits RX_DR
	# Data Ready RX FIFO interrupt. Asserted when
	#           new data arrives RX FIFOc.
	#           Write 1 to clear bit. 
	
	# Bits TX_DS
	# Data Sent TX FIFO interrupt. Asserted when
	#           packet transmitted on TX. If AUTO_ACK is acti-
	#           vated, this bit is set high only when ACK is
	#           received.
	#           Write 1 to clear bit. 
	
	# Bits MAX_RT
	# Maximum number of TX retransmits interrupt
	#           Write 1 to clear bit. If MAX_RT is asserted it must
	#           be cleared to enable further communication. 
	
	# Bits RX_P_NO
	# Data pipe number for the payload available for
	#           reading from RX_FIFO
	#           000-101: Data Pipe Number
	#           110: Not Used
	#           111: RX FIFO Empty 
	
	# Bits TX_FULL
	# TX FIFO full flag.
	#           1: TX FIFO full.
	#           0: Available locations in TX FIFO. 
	
	# Register OBSERVE_TX
	# Transmit observe register 
	
	def setOBSERVE_TX(self, val):
		"""Set register OBSERVE_TX"""
		self.write(REG.OBSERVE_TX, val, 8)
	
	def getOBSERVE_TX(self):
		"""Get register OBSERVE_TX"""
		return self.read(REG.OBSERVE_TX, 8)
	
	# Bits PLOS_CNT
	# Count lost packets. The counter is overflow pro-
	#           tected to 15, and discontinues at max until reset.
	#           The counter is reset by writing to RF_CH. See
	#           page 75. 
	
	# Bits ARC_CNT
	# Count retransmitted packets. The counter is reset
	#           when transmission of a new packet starts. See
	#           page 75. 
	
	# Register RPD
	
	
	def setRPD(self, val):
		"""Set register RPD"""
		self.write(REG.RPD, val, 8)
	
	def getRPD(self):
		"""Get register RPD"""
		return self.read(REG.RPD, 8)
	
	# Bits Reserved_0
	# Bits RPD
	# Received Power Detector. This register is called
	#           CD (Carrier Detect) in the nRF24L01. The name is
	#           different in nRF24L01+ due to the different input
	#           power level threshold for this bit. See section 6.4
	#           on page 25. 
	
	# Register RX_ADDR_P0
	# Receive address data pipe 0. 5 Bytes maximum
	#       length. (LSByte is written first. Write the number of
	#       bytes defined by SETUP_AW) 
	
	
	def setRX_ADDR_P0(self, val):
		"""Set register RX_ADDR_P0"""
		self.write(REG.RX_ADDR_P0, val, 40)
	
	def getRX_ADDR_P0(self):
		"""Get register RX_ADDR_P0"""
		return self.read(REG.RX_ADDR_P0, 40)
	
	# Bits RX_ADDR_P0
	# Register RX_ADDR_P1
	# Receive address data pipe 1. 5 Bytes maximum
	#       length. (LSByte is written first. Write the number of
	#       bytes defined by SETUP_AW) 
	
	
	def setRX_ADDR_P1(self, val):
		"""Set register RX_ADDR_P1"""
		self.write(REG.RX_ADDR_P1, val, 40)
	
	def getRX_ADDR_P1(self):
		"""Get register RX_ADDR_P1"""
		return self.read(REG.RX_ADDR_P1, 40)
	
	# Bits RX_ADDR_P1
	# Register RX_ADDR_P2
	# Receive address data pipe 2. Only LSB. MSBytes
	#       are equal to RX_ADDR_P1[39:8] 
	
	
	def setRX_ADDR_P2(self, val):
		"""Set register RX_ADDR_P2"""
		self.write(REG.RX_ADDR_P2, val, 8)
	
	def getRX_ADDR_P2(self):
		"""Get register RX_ADDR_P2"""
		return self.read(REG.RX_ADDR_P2, 8)
	
	# Bits RX_ADDR_P2
	# Register RX_ADDR_P3
	# Receive address data pipe 3. Only LSB. MSBytes
	#       are equal to RX_ADDR_P1[39:8] 
	
	
	def setRX_ADDR_P3(self, val):
		"""Set register RX_ADDR_P3"""
		self.write(REG.RX_ADDR_P3, val, 8)
	
	def getRX_ADDR_P3(self):
		"""Get register RX_ADDR_P3"""
		return self.read(REG.RX_ADDR_P3, 8)
	
	# Bits RX_ADDR_P3
	# Register RX_ADDR_P4
	# Receive address data pipe 4. Only LSB. MSBytes
	#       are equal to RX_ADDR_P1[39:8] 
	
	
	def setRX_ADDR_P4(self, val):
		"""Set register RX_ADDR_P4"""
		self.write(REG.RX_ADDR_P4, val, 8)
	
	def getRX_ADDR_P4(self):
		"""Get register RX_ADDR_P4"""
		return self.read(REG.RX_ADDR_P4, 8)
	
	# Bits RX_ADDR_P4
	# Register RX_ADDR_P5
	# Receive address data pipe 5. Only LSB. MSBytes
	#       are equal to RX_ADDR_P1[39:8] 
	
	
	def setRX_ADDR_P5(self, val):
		"""Set register RX_ADDR_P5"""
		self.write(REG.RX_ADDR_P5, val, 8)
	
	def getRX_ADDR_P5(self):
		"""Get register RX_ADDR_P5"""
		return self.read(REG.RX_ADDR_P5, 8)
	
	# Bits RX_ADDR_P5
	# Register TX_ADDR
	# Transmit address. Used for a PTX device only.
	#       (LSByte is written first)
	#       Set RX_ADDR_P0 equal to this address to handle
	#       automatic acknowledge if this is a PTX device with
	#       Enhanced ShockBurstTM enabled. See page 75. 
	
	
	def setTX_ADDR(self, val):
		"""Set register TX_ADDR"""
		self.write(REG.TX_ADDR, val, 40)
	
	def getTX_ADDR(self):
		"""Get register TX_ADDR"""
		return self.read(REG.TX_ADDR, 40)
	
	# Bits TX_ADDR
	# Register RX_PW_P0
	
	
	def setRX_PW_P0(self, val):
		"""Set register RX_PW_P0"""
		self.write(REG.RX_PW_P0, val, 8)
	
	def getRX_PW_P0(self):
		"""Get register RX_PW_P0"""
		return self.read(REG.RX_PW_P0, 8)
	
	# Bits Reserved_0
	# Only '00' allowed 
	# Bits RX_PW_P0
	# Number of bytes in RX payload in data pipe 0 (1 to 32 bytes).
	#           0 Pipe not used
	#           1 = 1 byte
	#           ...
	#           32 = 32 bytes 
	
	# Register RX_PW_P1
	
	
	def setRX_PW_P1(self, val):
		"""Set register RX_PW_P1"""
		self.write(REG.RX_PW_P1, val, 8)
	
	def getRX_PW_P1(self):
		"""Get register RX_PW_P1"""
		return self.read(REG.RX_PW_P1, 8)
	
	# Bits Reserved_0
	# Only '00' allowed 
	# Bits RX_PW_P1
	# Number of bytes in RX payload in data pipe 1 (1 to 32 bytes).
	#           0 Pipe not used
	#           1 = 1 byte
	#           ...
	#           32 = 32 bytes 
	
	# Register RX_PW_P2
	
	
	def setRX_PW_P2(self, val):
		"""Set register RX_PW_P2"""
		self.write(REG.RX_PW_P2, val, 8)
	
	def getRX_PW_P2(self):
		"""Get register RX_PW_P2"""
		return self.read(REG.RX_PW_P2, 8)
	
	# Bits Reserved_0
	# Only '00' allowed 
	# Bits RX_PW_P2
	# Number of bytes in RX payload in data pipe 2 (1 to
	#           32 bytes).
	#           0 Pipe not used
	#           1 = 1 byte
	#           ...
	#           32 = 32 bytes 
	
	# Register RX_PW_P3
	
	
	def setRX_PW_P3(self, val):
		"""Set register RX_PW_P3"""
		self.write(REG.RX_PW_P3, val, 8)
	
	def getRX_PW_P3(self):
		"""Get register RX_PW_P3"""
		return self.read(REG.RX_PW_P3, 8)
	
	# Bits Reserved_0
	# Only '00' allowed 
	# Bits RX_PW_P3
	# Number of bytes in RX payload in data pipe 3 (1 to
	#           32 bytes).
	#           0 Pipe not used
	#           1 = 1 byte
	#           ...
	#           32 = 32 bytes 
	
	# Register RX_PW_P4
	
	
	def setRX_PW_P4(self, val):
		"""Set register RX_PW_P4"""
		self.write(REG.RX_PW_P4, val, 8)
	
	def getRX_PW_P4(self):
		"""Get register RX_PW_P4"""
		return self.read(REG.RX_PW_P4, 8)
	
	# Bits Reserved_0
	# Only '00' allowed 
	# Bits RX_PW_P4
	# Number of bytes in RX payload in data pipe 4 (1 to
	#           32 bytes).
	#           0 Pipe not used
	#           1 = 1 byte
	#           ...
	#           32 = 32 bytes 
	
	# Register RX_PW_P5
	
	
	def setRX_PW_P5(self, val):
		"""Set register RX_PW_P5"""
		self.write(REG.RX_PW_P5, val, 8)
	
	def getRX_PW_P5(self):
		"""Get register RX_PW_P5"""
		return self.read(REG.RX_PW_P5, 8)
	
	# Bits Reserved_0
	# Only '00' allowed 
	# Bits RX_PW_P5
	# Number of bytes in RX payload in data pipe 5 (1 to
	#           32 bytes).
	#           0 Pipe not used
	#           1 = 1 byte
	#           ...
	#           32 = 32 bytes 
	
	# Register FIFO_STATUS
	# FIFO Status Register 
	
	def setFIFO_STATUS(self, val):
		"""Set register FIFO_STATUS"""
		self.write(REG.FIFO_STATUS, val, 8)
	
	def getFIFO_STATUS(self):
		"""Get register FIFO_STATUS"""
		return self.read(REG.FIFO_STATUS, 8)
	
	# Bits Reserved_0
	# Only '0' allowed 
	# Bits TX_REUSE
	# Used for a PTX device
	#           Pulse the rfce high for at least 10Î¼s to Reuse last
	#           transmitted payload. TX payload reuse is active
	#           until W_TX_PAYLOAD or FLUSH TX is executed.
	#           TX_REUSE is set by the SPI command
	#           REUSE_TX_PL, and is reset by the SPI commands
	#           W_TX_PAYLOAD or FLUSH TX 
	
	# Bits TX_FULL
	# TX FIFO full flag. 1: TX FIFO full. 0: Available loca-
	#           tions in TX FIFO. 
	
	# Bits TX_EMPTY
	# TX FIFO empty flag.
	#           1: TX FIFO empty.
	#           0: Data in TX FIFO. 
	
	# Bits Reserved_1
	# Only '00' allowed 
	# Bits RX_FULL
	# RX FIFO full flag.
	#           1: RX FIFO full.
	#           0: Available locations in RX FIFO. 
	
	# Bits RX_EMPTY
	# RX FIFO empty flag.
	#           1: RX FIFO empty.
	#           0: Data in RX FIFO. 
	
	# Register DYNPD
	# Enable dynamic payload length 
	
	def setDYNPD(self, val):
		"""Set register DYNPD"""
		self.write(REG.DYNPD, val, 8)
	
	def getDYNPD(self):
		"""Get register DYNPD"""
		return self.read(REG.DYNPD, 8)
	
	# Bits Reserved_0
	# Only 2'b00 allowed 
	# Bits DPL_P5
	# Enable dynamic payload length data pipe 5.
	#           (Requires EN_DPL and ENAA_P5) 
	
	# Bits DPL_P4
	# Enable dynamic payload length data pipe 4.
	#           (Requires EN_DPL and ENAA_P4) 
	
	# Bits DPL_P3
	# Enable dynamic payload length data pipe 3.
	#           (Requires EN_DPL and ENAA_P3) 
	
	# Bits DPL_P2
	# Enable dynamic payload length data pipe 2.
	#           (Requires EN_DPL and ENAA_P2) 
	
	# Bits DPL_P1
	# Enable dynamic payload length data pipe 1.
	#           (Requires EN_DPL and ENAA_P1) 
	
	# Bits DPL_P0
	# Enable dynamic payload length data pipe 0.
	#           (Requires EN_DPL and ENAA_P0) 
	
	# Register FEATURE
	# Feature Register 
	
	def setFEATURE(self, val):
		"""Set register FEATURE"""
		self.write(REG.FEATURE, val, 8)
	
	def getFEATURE(self):
		"""Get register FEATURE"""
		return self.read(REG.FEATURE, 8)
	
	# Bits Reserved_0
	# Only 5'b00000 allowed 
	# Bits EN_DPL
	# Enables Dynamic Payload Length 
	# Bits EN_ACK_PAYd
	# Enables Payload with ACK 
